Application of Encode and Decod
 
The concept of combinational logic states that two or more input states define one or more output states. 
Combinational logic circuits are encoders and decoders. With the help of boolean algebra, we implement combinational logic.

Encode The phrase "encode" refers to the process of converting unambiguous data into a less understandable form of code, 
and the device that executes this activity is known as an ad Encoder. 
An encoder is a device that converts analog signals to digital signals or turns an active data signal into a coded message format. 
It's a combinational circuit that translates binary data in the form of 2N input lines into N output lines that reflect the input in N bit code.
When an encoder receives an input signal, the logic circuitry within it turns the signal into coded binary output.

Decode To decode is to execute the opposite operation: transforming a code into an unambiguous form code, 
and the device that does this operation is known as a Decoder.
A decoder is a combinational circuit similar to an encoder, but it operates in the opposite direction.
A decoder is a device that turns n lines of input into 2n lines of output and generates the original signal as output from the coded input signal.
Because it provides a high output only when all inputs are high, an AND gate can be utilized as the basic decoding element.

Encoding and decoding together can be used in the simple applications of storing passwords in the back end and
many other applications like cryptography which deals with keeping the information confidential.

Syntax: decode(encoding, error) / encode(encode, error) 
encoding: Specifies the encoding on the basis of which decoding has to be performed. 
error: Decides how to handle the errors if they occur, e.g ‘strict’ raises Unicode error in case of exception and ‘ignore’ ignores the errors that occurred.

A small demonstration of password application using the application of encoding and decode.
