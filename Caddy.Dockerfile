FROM library/caddy

COPY --from=local/portfolio-reflex /app/.web/_static /srv
ADD Caddyfile /etc/caddy/Caddyfile