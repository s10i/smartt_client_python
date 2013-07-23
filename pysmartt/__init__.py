# Magic line that makes everything work! :)
# This allows me to run the application script directly from the package
# directory - I still don't understand how it works
# Got it from here: https://github.com/srid/modern-package-template
__import__('pkg_resources').declare_namespace(__name__)
