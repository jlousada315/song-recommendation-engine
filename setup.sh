mkdir -p ~/.streamlit/
echo "[general]
email = \"joao.lousada1@gmail.com\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml