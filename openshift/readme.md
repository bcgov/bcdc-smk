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


