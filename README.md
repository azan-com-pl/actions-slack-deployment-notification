# GitHub Action for sending Slack deployment notifications

Example:

```yaml
  - name: Send Slack notification on start
    uses: azan-com-pl/actions-slack-deployment-notification@main
    id: slack
    with:
      slack-channel-id: ${{ vars.SLACK_CHANNEL_ID }}
      slack-bot-token: ${{ secrets.SLACK_BOT_TOKEN }}
      environment-name: ${{ vars.ENVIRONMENT_NAME }}
      environment-url: ${{ vars.ENVIRONMENT_URL }}
      service: ${{ vars.SERVICE }}
      cluster: ${{ vars.CLUSTER }}
      release-tag: ${{ inputs.release_tag }}
      action: start

  - name: Send Slack notification on success
    uses: azan-com-pl/actions-slack-deployment-notification@main
    with:
      # ...
      action: success
      update-ts: ${{ steps.slack.outputs.ts }} # Update previous message instead of creating new one 
    if: ${{ success() }}
  
  - name: Send Slack notification on failure
    uses: azan-com-pl/actions-slack-deployment-notification@main
    with:
      # ...
      action: failure
      update-ts: ${{ steps.slack.outputs.ts }} # Update previous message instead of creating new one
    if: ${{ failure() }}
```

## Running tests

```sh
brew install bash_unit
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
bash_unit tests/*.sh
```
