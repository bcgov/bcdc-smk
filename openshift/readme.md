# About build...

* Build takes place on github [link to repo](https://github.com/bcgov/bcdc-smk)
* [Build action](https://github.com/bcgov/bcdc-smk/blob/master/.github/workflows/build.yaml)
* Images are stored as packages [link to package](https://github.com/bcgov/bcdc-smk/packages/356117)

# About Deploy

* template is defined [here:](https://github.com/bcgov/bcdc-smk/tree/master/openshift/deployTemplate.yaml)
* Example command to create what is defined in the template:
`oc process -f <github raw reference to deployTemplate.yaml> -p ENV='dev' -p | oc create -f -"`
* Same command but local reference to the template file:
`oc process -f ./deployTemplate.yaml -p ENV=dev | oc create -f -`


# GHA 

* link for sharing between steps:
   * https://stackoverflow.com/questions/58675200/in-github-actions-can-i-return-back-a-value-to-be-used-as-a-condition-later
   * https://github.com/marketplace/actions/persist-data-between-jobs
   * https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#jobsjob_idneeds


# Create Service Account
oc create sa ghadeploy

# Add edit role to user
oc policy add-role-to-user edit "system:serviceaccount:dbc-kirk-tools:ghadeploy"

# when logging in use second api  key that was created.  First is for internal access
# second is for external access.

finally update the image secrets to that the service account has access to the 
secret with the image stream, did this by editing the yaml for the service
account


# DEPLOY

$ oc process -f ./deployTemplate.yaml -p ENV=dev -p IMAGE_LABEL=20200818-1726 | oc replace -f -

# links
* [github actions openshift package](https://github.com/redhat-developer/openshift-actions)
* [example of template with service account and role](https://github.com/bcgov/repomountie/blob/master/openshift/templates/cicd.yaml)
* [openshift cheat sheet](https://design.jboss.org/redhatdeveloper/marketing/openshift_cheatsheet/cheatsheet/images/openshift_cheat_sheet_r1v1.pdf)
* [RBAC documentation](https://docs.openshift.com/container-platform/3.11/admin_guide/manage_rbac.html#creating-local-role)
* [openshift authorization docs - anchor goes to roles](https://docs.openshift.com/container-platform/3.11/architecture/additional_concepts/authorization.html#roles)
* [info on creating roles](https://docs.openshift.com/container-platform/3.11/admin_guide/manage_rbac.html#viewing-local-roles-and-bindings)
* [example deploy pipeline used for ckan](https://gogs.data.gov.bc.ca/bcdc/deployment/src/branch/master/ocp/.openshift/bcdc-ckan-ext-cicd.yaml)


# plan
1. create build in github actions
1. create secret that can access github packages (image stream secret) and enter into 
   openshift, named **bcdc-smk-image-access-secret**
1. create template for objects 
1. create service account **dbc-kirk-tools / ghadeploy**
1. allow service account access to the image secret (edit account yaml)
1. (later) - get service account and role assignement into template
1. github actions - create secrets for openshift url and openshift api token



# Troubleshooting

## Rollback a deployment
oc rollout <tag of image to be rolled out> dc/bcdcsmk-dev-dc -n <oc namespace>

### monitor rollout

#### Example link to deploy template using url

oc process -f https://raw.githubusercontent.com/bcgov/bcdc-smk/dev/openshift/deployTemplate.yaml  -p ENV=dev -p IMAGE_LABEL=20200821-1547 | oc replace -n dbc-kirk-tools -f -

#### Example link to deploy template using local file reference
oc process -f ./openshift/deployTemplate.yaml -p ENV=dev -p IMAGE_LABEL=20200821-1547 | oc replace -n dbc-kirk-tools -f -


#### Glueing it together:

* processing template pipeing into...
* oc replace
* finally oc rollout status that waits for it to complete.

