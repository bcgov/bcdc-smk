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