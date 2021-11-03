mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
[theme]\n\
primaryColor='#8cdc73'\n\
backgroundColor='#38318c'\n\
secondaryBackgroundColor='#1f196d'\n\
textColor='#ffffff'\n\
" > ~/.streamlit/config.toml