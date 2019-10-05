---
layout: default
title: Past Events
permalink: /past_events.html
---
<section class="container custom-height">
  <div class="row offset-positive">
    <div class="col">
      <h1 class="text-center my-5"> Past Events </h1>
    </div>
  </div>    

  {% assign post_count = site.categories.Past | size %}

  {% if post_count <= 0 %}

  <div class="row mb-5">
    <div class="col-12">
      <p class="rss-subscribe text-center small mb-0" style="margin-top: -20px">None so far. Go to <a href="/">home</a></p>
    </div>
  </div>

  {% else %}

  {% for post in site.categories.Past %}
  <div class="row mb-5">
    <div class="col-12">
      <div class="row">
        <div class="col-12 col-md-4">
          <img class="rounded w-100" src="/assets/img/events/{{post.img}}" alt="{{post.title}} Image">
        </div>
        <div class="col-12 col-md-8">
          <h3 class="mt-4">{{post.title}}</h3>
          <time class="lead small text-muted" datetime="{{ post.date | date_to_xmlschema }}" itemprop="datePublished">
            {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y at %R" -%}
            {{ post.date | date: date_format }}
          </time>
          {% for tag in post.tags %}  
            <span class="badge badge-pill badge-info" style="min-width: 70px">{{tag}}</span>
          {% endfor %}
          <p class="card-text mt-4 mb-1">{{ post.content | markdownify | strip_html | truncatewords: 30 }}</p>
          <a class="card-link small" href="{{ post.url | relative_url }}">Read More</a>
        </div>
      </div>
    </div>
  </div>
  {% endfor %}

  <p class="rss-subscribe text-center small mb-0" style="margin-top: -20px">Subscribe <a href="/feed.xml">via RSS</a></p>  

  {% endif %}

</section>