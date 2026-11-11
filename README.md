# Mailbox Migration Evidence Checker Demo

This sample shows how to compare redacted folder counts and alias destinations after a mailbox migration. The 28-second walkthrough uses fictional data and the checker output from the included sample.

[Watch the walkthrough](https://github.com/robbzzilla/mailbox-evidence-checker-demo/releases/tag/demo-v1) | [Read the sample report](sample-review.md)

| Item | Expected | Observed |
| --- | --- | --- |
| F01 | 98 destination items after two approved exclusions | 98 items |
| A01 | Alias points to M01 | Alias points to M02 |
| F02 | No skipped items | One skipped item |
| F03 | Destination count available | Destination count missing |

A comparison depends on the administrator supplying complete reports taken at the same cutoff. Confirm message integrity and live delivery separately.

## Fixed-price mailbox migration review

For a Google Workspace to Microsoft 365 cutover, I review one batch of up to five mailboxes for **$250 USD**. The written report flags folder count differences, unresolved migration skips, and incorrect alias destinations. It includes one recheck. Delivery is within two business days of receiving the agreed redacted inputs.

[Request a written scope](mailto:orderreliabilitysprint@gmail.com?subject=GitHub%20mailbox%20review). Include the planned cutover date, number of mailboxes, and whether your administrator can export folder counts and alias mappings. Keep credentials, addresses, and raw mailbox reports out of the inquiry. The administrator runs any live delivery checks.
