# BCDC - SMK



<img src="https://lh3.googleusercontent.com/pw/ACtC-3dk3TY4s-RkVMy5vtgT7YerYV-KcShjEFrBdminjSZ5BynNTkCu1CNEVZep9SfG_4B73iNwW0T6_MLiFKkyaZtVDxH0IsPTq0iTMacStLz6aFdww3kgMau1dW_LlVs6DovWkpU0vU9WW82uenYaXjutSQ=w1242-h699-no?authuser=0" width=650><br><br>

This repository contains the code that run's the base SMK site that the
BC Data Catalog will use for map previews.

# How to update to a new SMK version

## Clone the repository

As the header suggests start by cloneing this repo, then go into the repo
directory, and make sure you are on the dev branch.  (The default repo
is configured to be dev so you should already be on it)

```
git clone https://github.com/bcgov/bcdc-smk
cd bcdc-smk
git checkout dev
```

## Update the package.json smk dependency reference

Go to the file `package.json`, find the line:

```
    "dependencies": {
        "smk": "1.0.0-beta.2",
        ...=
```

Update the text `1.0.0-beta.2` to whatever the latest version is

## Test the change

Delete the following files / directories if they exist in your repo directory, if you
haven't already built then they won't exist.

* package-lock.json
* node_modules

Install dependencies:

```
npm install
```

Start the web server:

```
node node_modules/http-server/bin/http-server
```

Navigate the url that the previous command generates and verify that the
map at that url displays.

## Build - Test - Deploy (CD/CI)

This is automated through github actions.  The image stream for bcdc-smk
is: https://github.com/bcgov/bcdc-smk/packages/402546/versions

To trigger a build / dev deploy commit changes, push to github and create a pull request.

#### Commit / push changes

To deploy stage and commit the changes you have made and push them up
to `origin`.

```
git add package.json
git commit -m "updating the SMK version used by BCDC-SMK site"
git push origin dev
```

#### Trigger CD/CI pipeline

The pipeline is configured to be triggered by a pull request.  Create a new
pull request **from:** *dev* **to:** *master*

Pipeline will:

1. create an image tag
2. create a new docker image
3. tags the docker image
4. deploys the image to a dev oc namespace
5. updates the pr request with the url to the newly deployed version of the app
6. sends reviewers a notification letting them know we are awaiting a review

pr. closed and merged to master

1. deploys the image to prod
2. tags the merged commit with the image tag
3. deploys to prod
4. deletes the dev env.

<br><br><img src="https://acdc-tributeband.com/wp-content/uploads/logo.png">
