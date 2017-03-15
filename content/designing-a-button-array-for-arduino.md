---
Title: Designing a button array for Arduino
Date: 2017-03-15 10:37:08 PHT+0800
Category: Hardware
Slug: designing-a-button-array-for-arduino
Tags: arduino,buttons,circuit
Authors: Blue Cuenca
Summary: Design a circuit contaning an array of buttons connected to a single arduino pin
---

<!-- start here -->


I found [this arduino library][1] that process buttons connected to a single analog pin.


I designed a circuit that balances the interval for the values of the resistor ladder.  I hope that it would be easier to specify the values.  Instead, of reading the values, I would just specify the nominal values of 0 to 1023, with intervals of 102.

I have not tested the circuit yet, but it looks like this:

![buttons_array][2]




[1]: https://github.com/dxinteractive/AnalogMultiButton
[2]: {filename}/images/MultiButtonsDesign-med.png
