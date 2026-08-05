# Submitted Post-Change Sample Test TST-247

- Referenced issue: CQ-274
- Test author: Jonah Bell, Control Operations Analyst
- Test date: 2026-05-19
- Claimed test period: 2026-05-21 through 2026-06-15
- Population stated: 25 requests
- Sample reviewed: 20 requests
- Conclusion: Pass

## Method

The tester selected twenty request identifiers from a spreadsheet supplied by the remediation owner and checked whether manager and application-owner approval fields were populated.

## Results

- 18 requests contained both approval records.
- 2 requests contained manager approval but no application-owner approval attachment.
- 5 requests in the stated population were not tested.
- The workpaper does not show ticket creation dates, fulfillment dates, or evidence that the test was rerun after deployment.

## Independence note

The tester works in Control Operations and reports to the same director as the remediation owner. The supplied closure standard uses the term “independent test” but does not define organizational independence.

## Submitted conclusion

The workflow is operating effectively and REQ-03 is satisfied.
