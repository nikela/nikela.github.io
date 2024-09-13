---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<i>You can also find my articles on <u><a href="https://scholar.google.com/citations?user=LJ1SVE0AAAAJ">my Google
Scholar profile</a>.</u></i>

{% include base_path %}
{% assign publications = site.publications | sort: "year" |reverse  %}

{% for post in publications %}
  {% include publication-single.html %}
{% endfor %}
