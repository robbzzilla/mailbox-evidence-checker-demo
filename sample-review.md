# Mailbox Migration Evidence Review

Fictional example from Order Reliability Sprint. One mailbox reviewed at the November 11, 2026, 18:00 UTC reporting cutoff. Folder and alias labels are fictional.

## Findings

| Item | Finding | Evidence |
| --- | --- | --- |
| F01 | Matched | The source has 100 items. After two approved exclusions, 98 are expected and 98 appear at the destination. |
| A01 | Exception | The approved destination is M01. The observed alias points to M02. |
| F02 | Review skips | The expected count and destination count are both 98. The migration report records one skip. |
| F03 | Unverified | The source implies 98 items. The destination count is missing. |

## Evidence needed for the recheck

1. Confirm the approved destination for A01 and provide the updated alias export after any correction.
2. Record the disposition of the skipped F02 item and check it against the approved exclusions.
3. Provide the destination count for F03 at the agreed reporting cutoff.

The recheck covers these three items. Folder counts show aggregate agreement for the reviewed folders. The migration administrator verifies message integrity and live mail flow.

## Check your export fields

This fictional input comes from the checker's example batch. The two
timestamps use different offsets for the same reporting cutoff.

```json
{
  "source_cutoff": "2026-11-11T18:00:00Z",
  "target_cutoff": "2026-11-11T12:00:00-06:00",
  "checks": [
    {
      "mailbox": "M01",
      "kind": "folder",
      "item": "F02",
      "coverage_confirmed": true,
      "source_count": 100,
      "approved_exclusions": 2,
      "target_count": 98,
      "skipped_items": 1
    },
    {
      "mailbox": "M01",
      "kind": "alias",
      "item": "A01",
      "coverage_confirmed": true,
      "expected_target": "M01",
      "observed_target": "M02"
    }
  ]
}
```

The **F02** result is **review skips**. Both counts are 98, and the
migration report still has one skipped item to review. **A01** is an
**exception** because it points to M02 instead of the approved M01.
Use substitute labels for both alias destinations. Use `null` when the
observed destination is missing from the evidence. Use `MISSING_ALIAS`
only when a complete export confirms that the alias is absent.

Set `coverage_confirmed` to true after checking that both records cover
the same item and cutoff. Keep real mailbox addresses and records out
of your first message.

[Request a written review scope](README.md#fixed-price-mailbox-migration-review)

[Request the $39 offline checker](README.md#request-the-offline-checker-for-your-team)
