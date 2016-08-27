web: gunicorn betly.app:create_app\(\) -b 0.0.0.0:$PORT -w 3
build: npm install --only-dev
build: ENV=production ./node_modules/.bin/gulp build
