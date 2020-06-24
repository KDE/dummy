# Proposal

## invent:kde/ci-tools repository

- Have different gitlab-ci.yamls
    - gitlab-ci-frameworks.yaml
        - includes SuseQt5.10
        - includes SuseQt5.11
        - includes FreeBSDQt5.11
        - ...
    - gitlab-ci-applications.yaml
    - gitlab-ci-plasma.yaml
    - binary-factory-website-jekyll.yaml
    - binary-factory-website-sphinx.yaml
    - binary-factory-apk.yaml
    - binary-factory-dmg.yaml
    - binary-factory-flatpak.yaml
    - ...

# Framework repo
- Have a gitlab-ci.yaml
    - includes gitlab-ci-frameworks.yaml

# Application repo
- Have a gitlab-ci.yaml
    - includes gitlab-ci-plasma.yaml
    - includes binary-factory-webpage.yaml if they have single page website
    - includes binary-factory-flatpak.yaml
    
# Website repo
- Have a gitlab-ci.yaml
    - includes binary-factory-website-jekyll.yaml

# Kirigami app repo
- Have a gitlab-ci.yaml
    - includes gitlab-ci-applications.yaml
    - includes binary-factory-apk.yaml

More testing please!
Maybe Round 2?
Maybe Round 3?
Round 4?
Timing test
