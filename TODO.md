# TODO - Ecommerce Web Application (FastAPI + Vanilla JS)

- [ ] Create clean folder structure (backend app + frontend)
- [ ] Implement FastAPI backend
  - [ ] JWT login endpoint: POST /api/auth/login
  - [ ] Products endpoint: GET /api/products
  - [ ] Cart endpoints (per-user in-memory storage)
    - [ ] GET /api/cart
    - [ ] POST /api/cart/items
    - [ ] DELETE /api/cart/items/{product_id}
  - [ ] Serve frontend static files from FastAPI
- [ ] Implement frontend
  - [ ] Login page
  - [ ] Product listing + add-to-cart
  - [ ] Cart page
  - [ ] API integration (fetch + JWT)
- [ ] Add Docker support
  - [ ] backend/Dockerfile
  - [ ] docker-compose.yml
- [ ] Run the application automatically after setup
- [ ] Verify by running `docker compose up --build` and opening http://localhost:8000

