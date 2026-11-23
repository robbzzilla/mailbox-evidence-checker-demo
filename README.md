# Mailbox Migration Evidence Checker Demo

This sample shows how to compare redacted folder counts and alias destinations after a mailbox migration. The 28-second walkthrough shows all four fictional checks. The sample ZIP includes the full written report and the JSON input and output for two of those checks.

[Watch the walkthrough](https://github.com/robbzzilla/mailbox-evidence-checker-demo/releases/tag/demo-v1) | [Read the sample report](sample-review.md) | [Download the fictional sample (ZIP)](https://github.com/robbzzilla/mailbox-evidence-checker-demo/releases/download/demo-v1/Mailbox-Evidence-Checker-Fictional-Sample.zip) | [See fictional checker results (PNG)](https://github.com/robbzzilla/mailbox-evidence-checker-demo/releases/download/demo-v1/Mailbox.Evidence.Checker.Preview.png)


[Request the $39 offline checker](#request-the-offline-checker-for-your-team) · [Request a $250 written review](#fixed-price-mailbox-migration-review)

| Item | Expected | Observed |
| --- | --- | --- |
| F01 | 98 destination items after two approved exclusions | 98 items |
| A01 | Alias points to M01 | Alias points to M02 |
| F02 | No skipped items | One skipped item |
| F03 | Destination count available | Destination count missing |

A comparison depends on the administrator supplying complete reports taken at the same cutoff. A blank alias destination leaves the mapping unverified. A complete destination export can establish that an alias is absent. Confirm message integrity and live delivery separately.

## Fixed-price mailbox migration review

For a Google Workspace to Microsoft 365 cutover, I review one batch of up to five mailboxes for **$250 USD**. The written report flags folder count differences, unresolved migration skips, and incorrect alias destinations. It includes one recheck. Delivery is within two business days after written scope approval and receipt of the complete agreed redacted inputs.

The written review is AI-assisted. Before you share records, we agree in writing on permitted tools and how to handle redacted evidence.

[Request a written scope](mailto:orderreliabilitysprint@gmail.com?subject=GitHub%20mailbox%20review&body=Hi%20Robert%2C%0D%0A%0D%0AI%27d%20like%20to%20request%20a%20written%20scope%20for%20a%20mailbox%20migration%20review.%0D%0A%0D%0APlanned%20cutover%20date%20and%20time%20zone%3A%0D%0ANumber%20of%20mailboxes%3A%0D%0AAvailable%20reports%20%28folder%20counts%2C%20skipped%20items%2C%20alias%20mappings%29%3A%0D%0AWhere%20did%20you%20find%20this%20offer%3F%20%28optional%29%3A). You can also email **orderreliabilitysprint@gmail.com** with the subject **GitHub mailbox review**. Include your cutover date and time zone, mailbox count, and which reports you have. Keep credentials, mailbox addresses, and raw mailbox reports out of the inquiry.

### Records to have ready

- Source and destination message counts for each mapped folder, taken at the same reporting cutoff. A Gmail conversation can contain several messages, so use counts of individual messages on both sides.
- The approved mapping of Gmail labels to destination folders. Keep Outlook categories separate from folder totals.
- The migration report’s skipped-item counts and any approved exclusions.
- Expected and observed alias destinations, using substitute labels.

We agree on the batch, review contact, payment terms, and how to share redacted records before you send them. The administrator runs any live delivery checks.

## Request the offline checker for your team

If your team wants to run its own evidence checks, request a one-time **$39 USD** purchase for internal use. The ZIP includes the offline checker, setup instructions, fictional inputs, and an expected JSON report. It requires Python 3.11 or later and reads a JSON file. After unpacking the checker, run `python mailbox_review.py --demo` to reproduce all four fictional results before reviewing your own data. Before ordering, check that your redacted reports can supply the [fields in the example JSON file](sample-review.md#check-your-export-fields). See the [JSON output for that fictional input](sample-result.json) before preparing your own file and running the checker locally.

The $39 offer covers one organization checking its own migration. For MSP client work, we confirm the permitted use and price in writing before you order.

[Request a written purchase](mailto:orderreliabilitysprint@gmail.com?subject=Mailbox%20checker%20purchase&body=Hi%20Robert%2C%0D%0A%0D%0AI%27d%20like%20to%20request%20a%20%2439%20purchase%20of%20the%20Mailbox%20Evidence%20Checker%20for%20our%20organization.%0D%0A%0D%0AOrganization%3A%0D%0AIntended%20use%20%28own%20migration%20or%20client%20work%29%3A%0D%0APurchase%20or%20billing%20contact%3A%0D%0AWhere%20did%20you%20find%20this%20offer%3F%20%28optional%29%3A) or email **orderreliabilitysprint@gmail.com** with the subject **Mailbox checker purchase**. Say you're interested in the checker and name your purchasing organization. We'll confirm the software terms, billing, and delivery in writing before an order.

### Use the checker on client migrations

[Request MSP client-use terms](mailto:orderreliabilitysprint@gmail.com?subject=Mailbox%20checker%20MSP%20licensing&body=Hi%20Robert%2C%0D%0A%0D%0AI%E2%80%99d%20like%20to%20request%20terms%20for%20using%20the%20Mailbox%20Evidence%20Checker%20on%20client%20migrations.%0D%0A%0D%0AMSP%20or%20company%20name%3A%0D%0AExpected%20number%20of%20client%20migrations%3A%0D%0AWhich%20teams%20need%20to%20run%20the%20checker%3A%0D%0ADecision-maker%20or%20purchasing%20role%3A%0D%0A%0D%0AI%E2%80%99ll%20keep%20client%20names%2C%20mailbox%20addresses%2C%20and%20exports%20out%20of%20this%20inquiry.). You can also email **orderreliabilitysprint@gmail.com** with the subject **Mailbox checker MSP licensing**. Tell us how many client migrations you expect and who would run the checker. Keep client names and reports out of your first message.
