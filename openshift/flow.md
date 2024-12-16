# Overview of CD/CI for this repo

## Repository INIT

Before anything can be run in a repository it needs to have the following
objects defined:

* gha-deploy-sa (service account)
* gha-imagepull-secret (image pull secret)

Below goes over the details of setting these up.


### Configure *gha-deploy-sa* secret

#### Configure a personal access token for a user that has WRITE access to the 
repository:  https://github.com/bcgov/bcdc-smk

#### Make sure the user access token has the following permissions:
* write:packages 
* read:packages
* Full control of private repositories


#### Create a Secret in the target openshift project space
* type: Image Secret
* secret name: bcdcsmk-image-secret
* Authentication: Image Registry Credentials
* Image Registry Server Address: ghcr.io/bcgov/bcdc-smk/bcdc-smk


#### Create a service account 

`oc create sa gha-deploy-sa`

#### Assign the service account the **edit** role

```
OC_NAMESPACE=<enter name space to create secret in>
oc project $OC_NAMESPACE
oc policy add-role-to-user edit "system:serviceaccount:$OC_NAMESPACE:gha-deploy-sa"
```

#### Append permissions to the role to view depolyments, services, routes

Create the role:
`oc create role ghadeploy-role --verb=get,list --resource=deploymentconfigs.apps.openshift.io,routes.route.openshift.io -n $OC_NAMESPACE`

Add the role to the service account
`oc policy add-role-to-user ghadeploy-role gha-depoloy-sa --role-namespace=$OC_NAMESPACE -n $OC_NAMESPACE`


#### Get the service account secret
* go to secrets
* find a secret that is prefixed by the name of the service account that was just created
* choose the second of the two, reveal secrets and grab the secrets token

Test the secret

```
SA_SECRET=<paste secret into env var>
oc login --token $SA_SECRET
```

if successful, then
`oc projects` should return at least one project
`oc whoami` should tell you the name of the service account that you logged in as 


Enter service account api key and add as secret to Github

* go to github repo
* select settings->secrets
* enter the secret, 
    * OPENSHIFT_TOKEN_DEV - name of secret for account tied to dev deploy
    * OPENSHIFT_TOKEN_PROD - name of secret for account tied to prod deploy 


#### Allow service account access to the image pull secret

Summary of what has been done already:
* Created the service account: **gha-deploy-sa**
* Created the image pull secret: **bcdcsmk-image-secret**

Finally now we will give the service account access to the image pull secret

`oc secrets link gha-deploy-sa bcdcsmk-image-secret --for=pull`

# Summary of flow

## Pull Request to Master

* Triggers the GITHUB workflow 'BUILD' which creates a container image
    * [BCDC-SMK Images](https://github.com/bcgov/bcdc-smk/packages/356117/versions)
    * Image is tagged with a datestamp, example (20200821-1547)
    * Pull request Issue also is tagged with the datestamp tag that aligns with the image name

## Dev Deployment

* The dev deployment event is defined as: [workflow_run](https://docs.github.com/en/actions/reference/events-that-trigger-workflows#workflow_run)
* it is triggered by the completion of the BUILD phase
* the deploy to dev will tag the pr ticket with the tag dev-deploy
* Checks to see if the objects defined in the template exist in the destination project, and if so deletes them
* processes and creates objects defined in the template
* extracts the https:// route from the route object
* adds the route to the issue associated with the PR.
* now waits for review to be completed
* (later add request for review)  [see this link](https://docs.github.com/en/rest/reference/pulls#review-requests)

## Need trigger for review completed!

* [event to use:](https://docs.github.com/en/actions/reference/events-that-trigger-workflows#pull_request_review)
* check that can be merged, if so then merge using api.
* can query the pr end point for the attribute 'mergeable_state'.

* need to determine if the review has been completed and the code has been
  approved.
* then verify that pr is in a mergeable state, and if so, merge
* if the pr is not automatically closed then close the PR.

## Prod Deployment
* Action to use PR / Closed.
* [see here](https://stackoverflow.com/questions/44159555/how-do-we-know-a-pull-request-is-approved-or-rejected-using-api-in-github)
* check that the pr was merged, and if so then proceed with prd deployment from master





# Other Misc Notes / Links:
* [persisting data between workflows](https://docs.github.com/en/actions/configuring-and-managing-workflows/persisting-workflow-data-using-artifacts)


* [great article on nitty gritty of GHA](https://alexwlchan.net/2019/03/creating-a-github-action-to-auto-merge-pull-requests/)

* [merge using actions](https://developers.sap.com/tutorials/webide-github-merge-pull-request.html)

* [get commit and pr status](https://dev.to/gr2m/github-api-how-to-retrieve-the-combined-pull-request-status-from-commit-statuses-check-runs-and-github-action-results-2cen)

* [catalog / list of actions](https://github.com/sdras/awesome-actions)

* [trigger using curl](https://goobar.io/2019/12/07/manually-trigger-a-github-actions-workflow/)