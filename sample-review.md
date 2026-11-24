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

[View the fictional JSON input](sample-input.json) · [View the checker's JSON output](sample-result.json).

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
the same item, count definition, and reporting cutoff. Keep real mailbox
addresses and records out of your first message.

### When a mailbox is split between primary and archive

One migration administrator [reported a zero in a filtered archive export](https://zaclohrenz.com/posts/2026/aug12/) because the older messages landed in a separately named folder. Use the full destination folder inventory to map each primary or archive folder to its source date range. Compare matching, nonoverlapping ranges using the same timestamp definition and reporting cutoff.

For example, if the source has 40 older messages and the destination export reports zero without confirming it covers the mapped archive folder, set `coverage_confirmed` to false. The checker reports **unverified**. A complete, comparable export that confirms zero reports an **exception**. [Exchange Online folder statistics](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/get-exomailboxfolderstatistics?view=exchange-ps) can include hidden items, so confirm what each report counts before treating the totals as comparable.

### When an alias is missing from a mailbox export

An alias address can belong to a shared mailbox, a group, a mail contact, or another mail-enabled recipient. Ask the administrator which recipient types the export covers and to confirm the destination at the agreed cutoff. [Microsoft documents address conflicts across recipient types](https://learn.microsoft.com/en-us/troubleshoot/exchange/email-alias/proxy-address-being-used).

For fictional alias A10, the expected destination is mailbox M01. If a mailbox-only export shows no match, use `null` and set `coverage_confirmed` to false. If the administrator confirms that A10 instead belongs to group G07, use `G07` with confirmed coverage and the checker will report an **exception**. Keep conflicting exports **unverified** until the administrator resolves them. Use `MISSING_ALIAS` after the administrator establishes absence across the agreed recipient scope.

## Review an Amazon WorkMail cutover

AWS ends support for Amazon WorkMail on March 31, 2027. Before retiring the source, have your administrator capture folder counts and alias mappings for the users, groups and resources in your migration. Compare the source and destination evidence at an agreed cutoff. [AWS end-of-support notice](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html) · [AWS alias inventory reference](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListAliases.html)

These findings came from running a separate fictional WorkMail migration example through the packaged checker.

| Item | Finding | Evidence |
| --- | --- | --- |
| A01 | Matched | The alias points to the expected group G01. |
| A02 | Exception | The alias points to mailbox M02. The approved destination is group G01. |
| A03 | Unverified | The destination export covers mailboxes only. Group alias coverage is unconfirmed. |
| A04 | Exception | A complete destination inventory confirms the alias for resource R01 is absent. |
| F01 | Review skips | The destination has all 103 expected items after exclusions. The migration report records one skip to review. |

Use substitute labels and prepare the [normalized JSON input](#check-your-export-fields) from administrator reports. The checker reports folder-count and alias findings. Your migration administrator verifies individual messages, contacts, and live delivery separately. [Review the $39 license and delivery terms](README.md#request-the-offline-checker-for-your-team) · [Request a written purchase](mailto:orderreliabilitysprint@gmail.com?subject=Mailbox%20checker%20purchase&body=Hi%20Robert%2C%0D%0A%0D%0AI%20would%20like%20to%20request%20the%20%2439%20Mailbox%20Evidence%20Checker%20after%20reading%20the%20Amazon%20WorkMail%20cutover%20example.%0D%0A%0D%0APurchasing%20organization%3A%0D%0AIntended%20use%20%28own%20migration%20or%20client%20work%29%3A%0D%0ABilling%20contact%3A%0D%0A).

## Use this review for your cutover

[Request the $250 written review](README.md#fixed-price-mailbox-migration-review) for one Google Workspace to Microsoft 365 migration batch of up to five mailboxes. You receive a findings report and one recheck. In your first inquiry, include the cutoff and the reports you have. Keep the records with your administrator until we agree on how to share redacted evidence.

[Request the $39 offline checker](README.md#request-the-offline-checker-for-your-team) if your team will run the checks locally for its own migration. The ZIP includes the runnable Python checker and fictional data so your team can reproduce the results before using its own redacted reports.
