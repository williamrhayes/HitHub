# HitHub

## What is HitHub?

Hithub is a Mini Martial Artists Web App.

## Contributing

Would you like to fix an issue or add a feature? Here's how:

### Retrieving the Files from GitHub
1. Fork this repository
2. Clone the forked repository (`git clone https://github.com/USERNAME/HitHub.git`)
3. Add an upstream URL (`git remote add upstream https://github.com/williamrhayes/HitHub.git`)

### Setting Up Local Development

#### Installing Docker
1. Download and install [Docker](https://www.docker.com/get-started/)
2. Run the desktop installer
3. Restart your computer and accept the terms and conditions
4. Make an account (preferably tied to your GitHub account)
5. Make sure Docker was installed correctly (`docker --version`)
6. Test and see if you can run Docker's test image to make sure it was correctly installed (`docker run hello-world`)
7. Once Docker is installed correctly, navigate to the HitHub folder containing the `Dockerfile` and build the image (`docker build .`)

#### Establishing Environment Variables
1. Create a new file called `.env` to store environment variables.
2. Generate a `DJANGO_SECRET_KEY` for development (`python -c "import secrets; print(secrets.token_hex(24))"`)
3. Add the following lines to your `.env` file:
```
export DJANGO_SECRET_KEY="YOUR_KEY_HERE"
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_STORAGE_BUCKET_NAME="hithub"
export AWS_S3_REGION_NAME="us-west-2"
export DEBUG=True
```
4. Reach out to kidbillyy to gain AWS credentials (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`)
5. Create a new file called `.gitignore` to avoid pushing certain code to GitHub. Add the following lines to this file:
```
.env
.venv
db.sqlite3
__pycache__/
```

#### Running a Local Development Server
1. Make sure the Docker desktop app (the Docker daemon) is up and running and your file path is in the same location as the HitHub Dockerfile
2. Start up the development server (`docker-compose up`)
3. Navigate to `http://127.0.0.1:8000/` in your webbrowser and you should see a local version of the app!

### Making Contributions
1. Create your own branch (`git checkout -b feature`)
2. Commit your changes (`git commit -m 'Added a new feature'`)
3. Push to your own branch (`git push origin branch_name`)
4. Open a pull request comparing against the `dev` branch

## License

Distributed under the MIT License. See `LICENSE` for more information.
