# Overview of CD/CI for this repo

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