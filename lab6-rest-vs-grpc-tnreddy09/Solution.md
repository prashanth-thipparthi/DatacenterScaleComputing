
Method			|REST add  | gRPC add | REST img | gRPC img | PING  | 
------------------------------------------------------------------------------
Local			|	3.807    |   0.5374	   |	    6.545     |	 5.15   | 0.045	    |
------------------------------------------------------------------------------
Same-Zone		|	 3.23  |	  0.620    |	   10.028     |	7.037   |	  0.3     |
------------------------------------------------------------------------------
Different Region	|	   |	      |	         |	   |	    |
------------------------------------------------------------------------------


By observing the above values we can conclude that gRPC is efficient compared to the REST APIs.
We can also observe that as the geographical distance of client and server increases then the latency also increases.
We have to consider above learnings while working or developing systems which span across the world.
