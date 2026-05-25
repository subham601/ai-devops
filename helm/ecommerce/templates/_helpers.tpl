{{- define "ecommerce.name" -}}
ecommerce
{{- end -}}

{{- define "ecommerce.fullname" -}}
{{ include "ecommerce.name" . }}
{{- end -}}

{{- define "ecommerce.labels" -}}
app: {{ include "ecommerce.name" . }}
{{- end }}



