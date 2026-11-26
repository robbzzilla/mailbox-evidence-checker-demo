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

[Share the fixed-price scope with your approver](MAILBOX-REVIEW.md).

For a Google Workspace to Microsoft 365 cutover, I review one batch of up to five mailboxes for **$250 USD**. The written report flags folder count differences, unresolved migration skips, and incorrect alias destinations. It includes one recheck. Delivery is within two business days after written scope approval and receipt of the complete agreed redacted inputs.

If your cutover involves a third-party mailbox you use through Gmail,
describe how you currently receive mail and which address you send from.
Google lists January 2027 for removing Gmailify, third-party POP fetching
on the web, and third-party Send as. Gmail and Google Workspace aliases
continue to work. Your administrator can use those details to plan live
delivery checks. [Google's transition timeline](https://support.google.com/mail/answer/17101213?hl=en&stay=)

The written review is AI-assisted. Before you share records, we agree in writing on permitted tools and how to handle redacted evidence.

[Request a written scope](mailto:orderreliabilitysprint@gmail.com?subject=GitHub%20mailbox%20review&body=Hi%20Robert%2C%0D%0A%0D%0AI%27d%20like%20to%20request%20a%20written%20scope%20for%20a%20mailbox%20migration%20review.%0D%0A%0D%0APlanned%20cutover%20date%20and%20time%20zone%3A%0D%0ANumber%20of%20mailboxes%3A%0D%0AAvailable%20reports%20%28folder%20counts%2C%20skipped%20items%2C%20alias%20mappings%29%3A%0D%0AWhere%20did%20you%20find%20this%20offer%3F%20%28optional%29%3A). You can also email **orderreliabilitysprint@gmail.com** with the subject **GitHub mailbox review**. Include your cutover date and time zone, mailbox count, and which reports you have. Keep credentials, mailbox addresses, and raw mailbox reports out of the inquiry.

### Records to have ready

- Source and destination message counts for each mapped folder, taken at the same reporting cutoff. A Gmail conversation can contain several messages, so use counts of individual messages on both sides.
- The approved mapping of Gmail labels to destination folders. Keep Outlook categories separate from folder totals.
- The migration report’s skipped-item counts and any approved exclusions.
- Expected and observed alias destinations, using substitute labels.

We agree on the batch, review contact, payment terms, and how to share redacted records before you send them. The administrator runs any live delivery checks.

## Request the offline checker for your team

The one-time **$39 USD** purchase covers the offline Python checker for one organization’s internal use. The ZIP includes setup instructions, fictional inputs, and an expected JSON report. It requires Python 3.11 or later. The bundled sample and demo ran successfully on Windows with Python 3.11, 3.12, and 3.14.

Use it after your administrator has exported and normalized mapped folder
counts, skipped items, and alias destinations at a shared cutoff. The
checker reads one JSON file locally and requires no mailbox sign-in.
For a written findings report and one recheck, [request the $250 review](#fixed-price-mailbox-migration-review).

Moving from Amazon WorkMail? [See the tested cutover example](sample-review.md#review-an-amazon-workmail-cutover).

1. Before ordering, [open the two-check sample input](sample-input.json) and [compare the expected findings](sample-result.json). Use the [export checklist](sample-review.md#check-your-export-fields) to see if your reports cover the same fields.
2. Use the written purchase request below. We agree on the license and billing in writing, then send the ZIP once payment is confirmed under those terms.
3. Unpack the ZIP and run `python mailbox_review.py --demo` for all four fictional checks. To reproduce the two-check example with the purchased checker, save the public sample input alongside the script and run `python mailbox_review.py --input sample-input.json`.

### Prepare folder counts from a spreadsheet

Use the free [CSV preparation script](prepare_folder_counts.py) with Python 3.11 or later. Once your administrator has mapped folders, redacted identifiers, and reviewed coverage, save a UTF-8 CSV with these headers. The following rows are fictional.

```csv
mailbox,item,coverage_confirmed,source_count,approved_exclusions,target_count,skipped_items
M01,F01,true,100,2,98,0
M01,F02,true,100,2,98,1
M01,F03,false,100,2,,
```

Save the script and CSV in the same folder. Run it with the actual cutoff and timezone offset for each report. Choose a new output filename.

```text
python prepare_folder_counts.py counts.csv --source-cutoff 2026-11-11T18:00:00Z --target-cutoff 2026-11-11T12:00:00-06:00 --output counts.json
```

The script prepares folder rows locally. Leave an unknown target count or skip count blank. Enter coverage as `true` only when the administrator has verified it. Prepare alias checks separately using the [JSON sample](sample-input.json). To compare the folder batch with the paid checker, run `python mailbox_review.py --input counts.json` from the folder containing both files.

### Verify the delivered file

The current paid archive is
`Mailbox Evidence Checker.zip` (4,074 bytes). Its SHA-256 is
`7ad755c11254fdca316120316a60c782185a3de133fc4d33f5762ab99fd7eb44`. This fingerprint is for the purchased checker.
The fictional sample ZIP linked above has its own fingerprint.

On Windows, run this from the folder containing your purchased ZIP.

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath '.\Mailbox Evidence Checker.zip'
```

Compare the returned hash with the value above before extracting the ZIP.
If it differs, reply in the purchase thread with the file name and observed
hash so we can verify the delivery.

For MSP client work, we confirm the permitted use and price in writing before you order.

[Request the $39 internal-use purchase](mailto:orderreliabilitysprint@gmail.com?subject=Mailbox%20checker%20purchase&body=Hi%20Robert%2C%0D%0A%0D%0AI%27d%20like%20to%20purchase%20the%20%2439%20Mailbox%20Evidence%20Checker%20for%20internal%20use%20by%20our%20organization.%0D%0A%0D%0APurchasing%20organization%3A%0D%0APerson%20or%20team%20approving%20payment%3A%0D%0ADelivery%20email%20%28if%20different%20from%20this%20address%29%3A%0D%0AWhere%20did%20you%20find%20this%20offer%3F%20%28optional%29%3A). If you write from your email app, send to **orderreliabilitysprint@gmail.com** with the subject **Mailbox checker purchase**. Include the purchasing organization, who approves payment, and the delivery email if it differs from the reply address. We confirm the use terms, total and payment instructions in that thread. Keep mailbox files and payment details out of the request. For use on client migrations, [request MSP terms](#use-the-checker-on-client-migrations).

### Use the checker on client migrations

For one client's Google Workspace to Microsoft 365 cutover, you can
[request the $250 written review](MAILBOX-REVIEW.md#request-a-written-scope).
It covers one batch of up to five mailboxes. We agree in writing who can
share redacted evidence, who accepts the report, and who pays.

For repeat use across client migrations, tell us which team would run the
checker and whether any client needs a copy. We agree on the allowed use
and price in writing before you order.

[Request MSP client-use terms](mailto:orderreliabilitysprint@gmail.com?subject=Mailbox%20checker%20MSP%20licensing&body=Hi%20Robert%2C%0D%0A%0D%0AI%E2%80%99d%20like%20to%20request%20terms%20for%20using%20the%20Mailbox%20Evidence%20Checker%20on%20client%20migrations.%0D%0A%0D%0AMSP%20or%20company%20name%3A%0D%0AExpected%20number%20of%20client%20migrations%3A%0D%0AWhich%20teams%20need%20to%20run%20the%20checker%3A%0D%0AWill%20any%20client%20need%20a%20copy%3F%0D%0ADecision-maker%20or%20purchasing%20role%3A%0D%0A%0D%0AI%E2%80%99ll%20keep%20client%20names%2C%20mailbox%20addresses%2C%20and%20exports%20out%20of%20this%20inquiry.). You can also email **orderreliabilitysprint@gmail.com** with the subject **Mailbox checker MSP licensing**. Include the expected number of migrations, who will run the checker, and whether any client needs a copy. Keep client names and reports out of your first message.
