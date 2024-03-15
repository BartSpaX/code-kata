# Nth Prime
[![Static Badge](https://img.shields.io/badge/Link-To%20Exercise-blue)](https://exercism.org/tracks/python/exercises/nth-prime)

## Instructions

Given a number n, determine what the nth prime is.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that 
the 6th prime is 13.

If your language provides methods in the standard library to deal with prime 
numbers, pretend they don't exist and implement them yourself.

### Exception messages

Sometimes it is necessary to raise an exception. When you do this, you should 
always include a **meaningful error message** to indicate what the source of 
the error is. This makes your code more readable and helps significantly with 
debugging. For situations where you know that the error source will be a 
certain type, you can choose to raise one of the built in error types, but 
should still include a meaningful message.

This particular exercise requires that you use the raise statement to "throw" a 
`ValueError` when the `prime()` function receives malformed input. Since this 
exercise deals only with positive numbers, any number < 1 is malformed. The 
tests will only pass if you both `raise` the `exception` and include a message 
with it.

To raise a `ValueError` with a message, write the message as an argument to the 
`exception` type:

```python
# when the prime function receives malformed input
raise ValueError('there is no zeroth prime')
```