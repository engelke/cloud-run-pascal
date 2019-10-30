# cloud-run-pascal

Example web service in Pascal, deployed via Google Cloud Run

[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)

This code demonstrates how to create and deploy a web service written
in Pascal, using Google Cloud Run. The Pascal program that provides
the service is wrapped in a small Python program that receives the
web requests, runs the Pascal program, and then creates a web response
containing the output of the Pascal program.

The web service is invoked via an HTTPS GET request with a single
query parameter, `number=value`, where value is an integer. It returns
the given value, converted to Roman numerals.

The Pascal program is very basic, and was adapted from an example in
Kathleen Jensen's and Niklaus Wirth's _Pascal User Manual and Report_,
published in 1974. It does not handle Roman numeral shortcuts, such
as IV for 4, instead using the long version in those cases, like IIII.

This is obviously not the way to create a Roman numeral web service
today, but there are legacy programs in a variety of languages not
supported in today's managed serverless platforms that would be useful
to have as web services. This example shows how to make that happen.