#!/usr/bin/python
# -*- coding: utf-8 -*-


import bs4
text = """
<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"
	xmlns:content="http://purl.org/rss/1.0/modules/content/"
	xmlns:wfw="http://wellformedweb.org/CommentAPI/"
	xmlns:dc="http://purl.org/dc/elements/1.1/"
	xmlns:atom="http://www.w3.org/2005/Atom"
	xmlns:sy="http://purl.org/rss/1.0/modules/syndication/"
	xmlns:slash="http://purl.org/rss/1.0/modules/slash/"
	xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
xmlns:rawvoice="http://www.rawvoice.com/rawvoiceRssModule/"
xmlns:googleplay="http://www.google.com/schemas/play-podcasts/1.0"
>

<channel>
	<title>IoT Podcast &#8211; Internet of Things</title>
	<atom:link href="https://iotpodcast.com/feed/" rel="self" type="application/rss+xml" />
	<link>https://iotpodcast.com</link>
	<description>with Stacey Higginbotham</description>
	<lastBuildDate>Thu, 14 Feb 2019 15:15:21 +0000</lastBuildDate>
	<language>en-US</language>
	<sy:updatePeriod>hourly</sy:updatePeriod>
	<sy:updateFrequency>1</sy:updateFrequency>
	<generator>https://wordpress.org/?v=5.0.3</generator>
<!-- podcast_generator="Blubrry PowerPress/7.4" mode="advanced" feedslug="feed" Blubrry PowerPress Podcasting plugin for WordPress (https://www.blubrry.com/powerpress/) -->
	<itunes:summary>Stacey Higginbotham has covered technology since 2001. In my years covering tech I became more fascinated by the stuff were were able to do on vast computing networks and ever speedier mobile and wireline broadband networks. Finally all of the elements of the technology I’ve covered in more than a decade have culminated in this moment and we’re creating the internet of things.&lt;br /&gt;
&lt;br /&gt;
No matter what you call it, we’re at a pivotal moment in the evolution of human creativity, business creation and productivity gains. We could see the gains we make in these next few years help us conserve resources and let us lead safer and healthier lives or we could open the door to a dystopian society where our every thought is monitored and our every utterance is effectively for sale. I hope to explore all of these issues, the people who will make it possible and the devices that will lead us there in the IoT Podcast. I hope you will join me.</itunes:summary>
	<itunes:author>Stacey Higginbotham, tech journalist</itunes:author>
	<itunes:image href="https://iotpodcast.com/wp-content/uploads/2015/07/IOT-podcast-12.png" />
	<itunes:owner>
		<itunes:name>Stacey Higginbotham, tech journalist</itunes:name>
		<itunes:email>higginbob@gmail.com</itunes:email>
	</itunes:owner>
	<managingEditor>higginbob@gmail.com (Stacey Higginbotham, tech journalist)</managingEditor>
	<copyright>Copyright Stacey Higginbotham 2018</copyright>
	<itunes:subtitle>The Internet of Things Podcast - Stacey on IoT</itunes:subtitle>
	<image>
		<title>IoT Podcast &#8211; Internet of Things</title>
		<url>https://iotpodcast.com/wp-content/uploads/2015/07/IOT-podcast-12.png</url>
		<link>https://iotpodcast.com</link>
	</image>
	<itunes:category text="Technology">
		<itunes:category text="Tech News"></itunes:category>
	</itunes:category>
	<itunes:category text="Technology">
		<itunes:category text="Gadgets"></itunes:category>
	</itunes:category>
	<itunes:category text="Technology">
		<itunes:category text="Software How-To"></itunes:category>
	</itunes:category>
	<googleplay:email>higginbob@gmail.com</googleplay:email>
	<googleplay:description>Stacey Higginbotham has covered technology since 2001. In my years covering tech I became more fascinated by the stuff were were able to do on vast computing networks and ever speedier mobile and wireline broadband networks. Finally all of the elements of the technology I’ve covered in more than a decade have culminated in this moment and we’re creating the internet of things.

No matter what you call it, we’re at a pivotal moment in the evolution of human creativity, business creation and productivity gains. We could see the gains we make in these next few years help us conserve resources and let us lead safer and healthier lives or we could open the door to a dystopian society where our every thought is monitored and our every utterance is effectively for sale. I hope to explore all of these issues, the people who will make it possible and the devices that will lead us there in the IoT Podcast. I hope you will join me.
</googleplay:description>
	<googleplay:category text="Technology" />
	<googleplay:image href="https://iotpodcast.com/wp-content/uploads/2015/07/IOT-podcast-12.png" />
	<rawvoice:rating>TV-G</rawvoice:rating>
	<rawvoice:frequency>Weekly</rawvoice:frequency>
	<rawvoice:subscribe feed="https://iotpodcast.com/feed/" itunes="https://itunes.apple.com/us/podcast/internet-things-podcast/id994362496"></rawvoice:subscribe>
	<item>
		<title>Episode 203: Amazon&#8217;s Eero buy and RISC-V</title>
		<link>https://iotpodcast.com/2019/02/episode-203-amazons-eero-buy-and-risc-v/</link>
		<comments>https://iotpodcast.com/2019/02/episode-203-amazons-eero-buy-and-risc-v/#respond</comments>
		<pubDate>Thu, 14 Feb 2019 10:00:03 +0000</pubDate>
		<dc:creator><![CDATA[Stacey Higginbotham]]></dc:creator>
				<category><![CDATA[cloud]]></category>
		<category><![CDATA[connected car]]></category>
		<category><![CDATA[enterprise]]></category>
		<category><![CDATA[industrial internet]]></category>
		<category><![CDATA[security]]></category>
		<category><![CDATA[smart home]]></category>
		<category><![CDATA[standards]]></category>
		<category><![CDATA[Abode]]></category>
		<category><![CDATA[ADT]]></category>
		<category><![CDATA[Amazon]]></category>
		<category><![CDATA[Arlo]]></category>
		<category><![CDATA[Eero]]></category>
		<category><![CDATA[Ford]]></category>
		<category><![CDATA[Google]]></category>
		<category><![CDATA[Greenwaves Technologies]]></category>
		<category><![CDATA[Hubitat]]></category>
		<category><![CDATA[RISC-V]]></category>
		<category><![CDATA[Samsung]]></category>
		<category><![CDATA[Samsung ARTIK]]></category>
		<category><![CDATA[Sigfox]]></category>
		<category><![CDATA[Urban-X]]></category>
		<category><![CDATA[Western Digital]]></category>

		<guid isPermaLink="false">https://iotpodcast.com/?p=1689</guid>
		<description><![CDATA[There were several acquisitions this week and the end of two prominent IoT platforms to cover, so Kevin and I had a lot to talk about. We kick off the show with Amazon&#8217;s purchase of mesh Wi-Fi company Eero and then segue into a conversation about Amazon&#8217;s data collection efforts. From there we move into security company &#8230; <a href="https://iotpodcast.com/2019/02/episode-203-amazons-eero-buy-and-risc-v/" class="more-link">Continue reading <span class="screen-reader-text">Episode 203: Amazon&#8217;s Eero buy and RISC-V</span></a>]]></description>
				<content:encoded><![CDATA[<p>There were several acquisitions this week and the end of two prominent IoT platforms to cover, so Kevin and I had a lot to talk about. We kick off the show with <a href="https://staceyoniot.com/amazon-just-acquired-eero-because-wi-fi-is-key-to-the-smart-home/" target="_blank" rel="noopener">Amazon&#8217;s purchase of mesh Wi-Fi company Eero</a> and then segue into a conversation about <a href="https://www.bloomberg.com/news/articles/2019-02-12/your-smart-light-can-tell-amazon-and-google-when-you-go-to-bed" target="_blank" rel="noopener">Amazon&#8217;s data collection efforts</a>. From there we move into security company <a href="https://www.cepro.com/article/adt_lifeshield_diy_home_security/news" target="_blank" rel="noopener">ADT buying a DIY security company</a> called LifeShield, and then DIY security company <a href="https://www.multichannel.com/pr-feed/abode-partners-with-hellotech-to-augment-whole-home-automation-and-security-offerings-with-do-it-for-me-installation-services" target="_blank" rel="noopener">abode entering into a partnership</a> with do-it-for-me helper Hello Tech. After that, we talk about <a href="https://android-developers.googleblog.com/2019/02/an-update-on-android-things.html" target="_blank" rel="noopener">Google&#8217;s demotion of the Android Things</a> platform and the <a href="http://www.businesskorea.co.kr/news/articleView.html?idxno=27384" target="_blank" rel="noopener">end</a> of Samsung&#8217;s Artik module and <a href="https://developer.artik.io/" target="_blank" rel="noopener">cloud</a>.  We cover <a href="https://build.sigfox.com/sigfox-device-radio-specifications" target="_blank" rel="noopener">news from Sigfox</a>, a <a href="https://www.wareable.com/smartwatches/sony-wena-wrist-pro-active-price-specs-release-date-6980" target="_blank" rel="noopener">new wearable</a>, and <a href="https://www.cepro.com/article/arlo_2018_report_2019_outlook" target="_blank" rel="noopener">Arlo&#8217;s earnings</a> before getting <a href="https://staceyoniot.com/hubitat-elevation-review/" target="_blank" rel="noopener">Kevin&#8217;s thoughts on the Hubitat Elevation hub</a>. And we end by answering a listener question on how to prevent smart TVs from <a href="https://www.consumerreports.org/privacy/how-to-turn-off-smart-tv-snooping-features/" target="_blank" rel="noopener">spying</a> on you.</p>
<figure id="attachment_1690" style="width: 800px" class="wp-caption aligncenter"><a href="https://iotpodcast.com/wp-content/uploads/2019/02/fordsmartbed.jpg"><img class="size-full wp-image-1690" src="https://iotpodcast.com/wp-content/uploads/2019/02/fordsmartbed.jpg" alt="" width="800" height="568" srcset="https://iotpodcast.com/wp-content/uploads/2019/02/fordsmartbed.jpg 800w, https://iotpodcast.com/wp-content/uploads/2019/02/fordsmartbed-300x213.jpg 300w, https://iotpodcast.com/wp-content/uploads/2019/02/fordsmartbed-768x545.jpg 768w" sizes="(max-width: 800px) 100vw, 800px" /></a><figcaption class="wp-caption-text"><a href="https://www.autoblog.com/2019/02/12/fords-smart-bed-unruly-sleepers/" target="_blank" rel="noopener">Ford&#8217;s smart bed concept</a> uses lane-change detection to wrangle restless sleepers.</figcaption></figure>
<p>Our guest this week is Loic Lietar, CEO of <a href="https://greenwaves-technologies.com/" target="_blank" rel="noopener">Greenwaves Technologies</a>, a chip design firm using the new open-source RISC-V architecture to design a low-power IoT processor. Lietar explains what RISC-V is, how difficult it is to get the industry to adopt a new processor architecture and what RISC-V could mean for the IoT. He also discusses how the economics of open source silicon could change how chips get adopted and designed. You&#8217;ll want to tune in.</p>
<p><strong>Host</strong>: Stacey Higginbotham and Kevin Tofel<br />
<strong>Guest</strong>: Loic Lietar, CEO of <a href="https://greenwaves-technologies.com/" target="_blank" rel="noopener">Greenwaves Technologies</a><br />
<strong>Sponsors</strong>: <a href="http://www.urban-x.com/apply" target="_blank" rel="noopener">Urban-X</a> and <a href="http://www.westerndigital.com" target="_blank" rel="noopener">Western Digital</a></p>
<ul>
<li>Why Amazon bought Eero and other routers you might choose now</li>
<li>The death of Samsung Artik and the demotion of Android Things</li>
<li><a href="https://staceyoniot.com/hubitat-elevation-review/" target="_blank" rel="noopener">Hubitat Elevation hub review</a></li>
<li>Why is <a href="https://www.autoblog.com/2019/02/12/fords-smart-bed-unruly-sleepers/" target="_blank" rel="noopener">Ford making a bed</a>?</li>
<li>What the heck is RISC-V</li>
<li>Why does the world need a new instruction set?</li>
</ul>
]]></content:encoded>
			<wfw:commentRss>https://iotpodcast.com/2019/02/episode-203-amazons-eero-buy-and-risc-v/feed/</wfw:commentRss>
		<slash:comments>0</slash:comments>
<enclosure url="https://dts.podtrac.com/redirect.mp3/traffic.libsyn.com/iotpodcast/IOT203.mp3" length="47303049" type="audio/mpeg" />
		<itunes:subtitle>There were several acquisitions this week and the end of two prominent IoT platforms to cover, so Kevin and I had a lot to talk about. We kick off the show with Amazon’s purchase of mesh Wi-Fi company Eero and then segue into a conversation about Amazo...</itunes:subtitle>
		<itunes:summary>There were several acquisitions this week and the end of two prominent IoT platforms to cover, so Kevin and I had a lot to talk about. We kick off the show with Amazon’s purchase of mesh Wi-Fi company Eero and then segue into a conversation about Amazon’s data collection efforts. From there we move into security company … Continue reading Episode 203: Amazon’s Eero buy and RISC-V</itunes:summary>
		<itunes:author>Stacey Higginbotham, tech journalist</itunes:author>
		<itunes:image href="https://iotpodcast.com/wp-content/uploads/2015/07/IOT-podcast-12.png" />
		<itunes:duration>56:07</itunes:duration>
	</item>
		<item>
		<title>Episode 202: What happens when your smart home gets a subpoena</title>
		<link>https://iotpodcast.com/2019/02/episode-202-what-happens-when-your-smart-home-gets-a-subpoena/</link>
		<comments>https://iotpodcast.com/2019/02/episode-202-what-happens-when-your-smart-home-gets-a-subpoena/#comments</comments>
		<pubDate>Thu, 07 Feb 2019 10:00:10 +0000</pubDate>
		<dc:creator><![CDATA[Stacey Higginbotham]]></dc:creator>
... """
soup = bs4.BeautifulSoup(text, 'html.parser')
print(soup.select('item:nth-of-type(1) title'))