---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find my articles on <u><a href="https://scholar.google.com/citations?user=LJ1SVE0AAAAJ">my Google Scholar profile</a>.</u>

{% include base_path %}
{% assign publications = site.publications | sort: "year" |reverse  %}

{% for post in publications %}
  {% include archive-single.html %}
{% endfor %}
