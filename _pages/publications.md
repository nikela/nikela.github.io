---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>

{% include base_path %}
{% assign publications = site.publications | sort: "year" |reverse  %}

{% for post in publications %}
  {% include archive-single.html %}
{% endfor %}
