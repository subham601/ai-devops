/* global window */

const App = {
  tokenKey: 'access_token',

  get token() {
    return window.localStorage.getItem(this.tokenKey);
  },

  set token(val) {
    if (val) window.localStorage.setItem(this.tokenKey, val);
    else window.localStorage.removeItem(this.tokenKey);
  },

  headers() {
    if (!this.token) return {};
    return { Authorization: `Bearer ${this.token}` };
  },

  setLogoutHandlers() {
    const btn = document.getElementById('logoutBtn');
    if (!btn) return;
    btn.addEventListener('click', () => {
      this.token = null;
      window.location.href = '/login.html';
    });
  },

  async apiJson(path, opts = {}) {
    const res = await fetch(path, {
      headers: {
        'Content-Type': 'application/json',
        ...this.headers(),
        ...(opts.headers || {}),
      },
      ...opts,
    });

    let data = null;
    try {
      data = await res.json();
    } catch (_) {}

    if (!res.ok) {
      const msg = (data && data.detail) ? data.detail : `HTTP ${res.status}`;
      throw new Error(msg);
    }
    return data;
  },

  async init() {
    this.setLogoutHandlers();

    const page = window.__PAGE__ || 'products';
    if (page === 'login') return this.initLogin();
    if (!this.token) {
      window.location.href = '/login.html';
      return;
    }
    if (page === 'cart') return this.initCart();
    return this.initProducts();
  },

  initLogin() {
    const btn = document.getElementById('loginBtn');
    const err = document.getElementById('error');
    const emailEl = document.getElementById('email');
    const passEl = document.getElementById('password');

    if (!btn) return;

    btn.addEventListener('click', async () => {
      err.textContent = '';
      btn.disabled = true;
      try {
        const payload = {
          email: emailEl.value,
          password: passEl.value,
        };
        const data = await this.apiJson('/api/auth/login', {
          method: 'POST',
          body: JSON.stringify(payload),
          headers: { 'Content-Type': 'application/json' },
        });
        this.token = data.access_token;
        window.location.href = '/';
      } catch (e) {
        err.textContent = String(e.message || e);
      } finally {
        btn.disabled = false;
      }
    });
  },

  initProducts() {
    const status = document.getElementById('status');
    const root = document.getElementById('products');
    if (!root) return;

    status.textContent = 'Loading products...';

    this.apiJson('/api/products')
      .then((data) => {
        const items = data.items || [];
        root.innerHTML = items
          .map((p) => {
            return `
              <div class="product">
                <h3>${this.escapeHtml(p.name)}</h3>
                <p>${this.escapeHtml(p.description)}</p>
                <div class="price">$${Number(p.price).toFixed(2)}</div>
                <button class="btn" type="button" data-pid="${p.id}">Add to cart</button>
              </div>
            `;
          })
          .join('');

        root.querySelectorAll('button[data-pid]').forEach((btn) => {
          btn.addEventListener('click', async () => {
            const pid = Number(btn.getAttribute('data-pid'));
            btn.disabled = true;
            const prev = btn.textContent;
            btn.textContent = 'Adding...';
            try {
              await this.apiJson('/api/cart/items', {
                method: 'POST',
                body: JSON.stringify({ product_id: pid, quantity: 1 }),
              });
              // eslint-disable-next-line no-alert
              window.alert('Added to cart');
            } catch (e) {
              // eslint-disable-next-line no-alert
              window.alert(String(e.message || e));
            } finally {
              btn.disabled = false;
              btn.textContent = prev;
            }
          });
        });

        status.textContent = '';
      })
      .catch((e) => {
        status.textContent = String(e.message || e);
      });
  },

  async initCart() {
    const status = document.getElementById('cartStatus');
    const root = document.getElementById('cartItems');
    const totalEl = document.getElementById('cartTotal');
    if (!root || !totalEl) return;

    status.textContent = 'Loading cart...';

    try {
      const data = await this.apiJson('/api/cart');
      const items = data.items || [];

      if (!items.length) {
        root.innerHTML = '<div class="muted">Cart is empty.</div>';
        totalEl.textContent = '$0.00';
        status.textContent = '';
        return;
      }

      root.innerHTML = items
        .map((it) => {
          const lineTotal = Number(it.price) * Number(it.quantity);
          return `
            <div class="cart-item">
              <div>
                <div class="title">${this.escapeHtml(it.name)}</div>
                <div class="meta">$${Number(it.price).toFixed(2)} × ${it.quantity} = $${lineTotal.toFixed(2)}</div>
              </div>
              <div class="cart-actions">
                <button class="small-btn danger" type="button" data-remove="${it.product_id}">Remove</button>
              </div>
            </div>
          `;
        })
        .join('');

      root.querySelectorAll('button[data-remove]').forEach((btn) => {
        btn.addEventListener('click', async () => {
          const pid = Number(btn.getAttribute('data-remove'));
          btn.disabled = true;
          try {
            await this.apiJson(`/api/cart/items/${pid}`, { method: 'DELETE' });
            window.location.reload();
          } catch (e) {
            // eslint-disable-next-line no-alert
            window.alert(String(e.message || e));
            btn.disabled = false;
          }
        });
      });

      totalEl.textContent = `$${Number(data.total).toFixed(2)}`;
      status.textContent = '';
    } catch (e) {
      status.textContent = String(e.message || e);
    }
  },

  escapeHtml(str) {
    return String(str)
      .replaceAll('&', '&amp;')
      .replaceAll('<', '<')
      .replaceAll('>', '>')
      .replaceAll('"', '"')
      .replaceAll("'", '&#039;');
  },
};

window.App = App;

