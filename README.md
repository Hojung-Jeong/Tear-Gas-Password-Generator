# Tear-Gas-Password-Generator
Tear Gas Password Generator is a flexible and powerful password generator written in python 3
It contains true random number generator which generates randomness by intentionally making data corruption to generate passwords


#Install
Run the command below in case of Windows
>python3 setup.py install

Run the command below in case of Unix-based systems
>sudo python3 setup.py install

#Usage
>from teargas.passgen import passgen    
>print ( passgen() )

or it is possible to set the password length. Default value is 20
>from teargas.passgen import passgen    
>print ( passgen(32) )


#License
Apache License
