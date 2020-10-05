
## in general
* remove references to namespace
* no longer reference 


helm install  bcdc-smk-deployhelm ./bcdc-smk -f <config file>

where 


helm ls
shows what's been deployed
NAME                    NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
bcdc-smk-deployhelm     databcdc        1               2020-09-30 12:16:34.9680896 -0700 PDT   deployed        bcdc-smk-0.1.0  1.16.0     

bcdc-smk-deployhelm: name of chart
databcdc: oc namespace
bcdc-smk-0.1.0: chart and version that's deployed


