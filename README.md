# FindMe  

FindMe is a smart status indicator system created with Raspberry Pi and E-ink display. The project started in mid-August 2018 by Nitis Monburinon. The project is named by Prof. Zabir later and has become a regular project that we show to lab visitors presented during our demonstration session.

In Japan, usually, lecturers and researchers have customs to use something like whiteboard or paper to indicate their statuses in their workplaces. 

These indicators tell their visitors whether the lecturers are available or not. Are lecturers at lunch or having meetings? 

Are they home or working overtime? Visitors can tell by looking at indicators in front of the lecturers’ places.  

This system very useful in many situations and we thought we could improve its usefulness further by adding IOT and E-Ink technology to it. 

> Electronic ink technology produces a low-power paperlike display used primarily in early e-book readers such as Amazon's Kindle. Initial research on e-ink started at MIT's Media Lab, where the first patent was filed in 1996. 
The rights to the proprietary technology currently are owned by the Massachusetts-based E Ink Corporation, which was acquired by Taiwanese company Prime View International in 2009. E-ink technology in early e-readers works by using tiny microcapsules that are suspended in a liquid placed within a film layer. The microcapsules, which are about the same width as human hair, contain both positively charged white particles and negatively charged black particles. Applying a negative electrical field causes the white particles to come to the surface. Conversely, applying a positive electrical field causes the black particles to come to the surface. By applying different fields at various parts of a screen, e-ink produces a text display. E-ink displays are especially popular due to their resemblance to printed paper. Besides being considered by many as easier on the eyes than other display types, e-ink also boasts lower power consumption, particularly when compared to traditional backlit liquid crystal display (LCD) screens. 
Considering all the advantage E-ink displays provide, we adopt the technology in our FindMe project. FindMe can be deployed in front of any workplace or office. Users can use an Android mobile application to send messages to it from anywhere. 

As the display only refresh once it receives messages, power consumption is low. 

FindMe keeps texts on the display for a long time even when it’s not powered. This is useful when power is unavailable.

The E-ink display has its own low-level library written in C. But I have developed a high-level API that easily understandable using Python. 

At the current state, English, Japanese, and Thai were tested and proved to work correctly on the display.
