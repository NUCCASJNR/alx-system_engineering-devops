## Web stack debugging

![debugging](https://lh3.googleusercontent.com/6f4ZmY3rNNbMglzP53SuBFafJaX1AXEvviVIurhbxjzntDgcbJy5L2xCGP8t2oN-EBWYwGUpsGrG02p4jZ58yBvdH7hc38naolBBi23Xiw)


## Resources

## Network basics

- Networking is a big part of what made computers so powerful and why the Internet exists. It allows machines to communicate with each other.

[What is a protocol](https://www.techtarget.com/searchnetworking/definition/protocol)

[What is an IP address](https://computer.howstuffworks.com/internet/basics/what-is-an-ip-address.htm)

[What is TCP/IP](https://www.avast.com/c-what-is-tcp-ip#)

[What is an Internet Protocol (IP) port?](https://www.lifewire.com/port-numbers-on-computer-networks-817939)


## Web stack debugging

- Intro

. Debugging usually takes a big chunk of a software engineer’s time. The art of debugging is tough and it takes years, even decades to master, and that is why seasoned software engineers are the best at it… experience. They have seen lots of broken code, buggy systems, weird edge cases and race conditions

![web](https://lh3.googleusercontent.com/H1el2aXQu0OtlIYw7pKeNJ6OyzxYTqW6ZxmT3VMoe2AMHPLg-nFEpbZgBuy0Q1JdNOTu8xnuF-Vp1YzMSbGJzq58IsDw8z5RoaY3B2A)

## Non-exhaustive guide to debugging

## School specific

- If you are struggling to get something right that is run on the checker, like a Bash script or a piece of code, keep in mind that you can simulate the flow by starting a Docker container with the distribution that is specified in the requirements and by running your code. Check the Docker concept page for more info.

## Test and verify your assumptions

- The idea is to ask a set of questions until you find the issue. For example, if you installed a web server and it isn’t serving a page when browsing the IP, here are some questions you can ask yourself to start debugging:

- Is the web server started? - You can check using the service manager, also double check by checking process list.
- On what port should it listen? - Check your web server configuration
- Is it actually listening on this port? - netstat -lpdn - run as root or sudo so that you can see the process for each listening port
- It is listening on the correct server IP? - netstat is also your friend here
- Is there a firewall enabled?
- Have you looked at logs? - usually in /var/log and tail -f is your friend
- Can I connect to the HTTP port from the location I am browsing from? - curl is your friend
- There is a good chance that at this point you will already have found part of the issue.

## Get a quick overview of the machine state

[Youtube video First 5 Commands When I Connect on a Linux Server](https://www.youtube.com/watch?v=1_gqlbADaAw&feature=youtu.be)

- When you connect to a server/machine/computer/container you want to understand what’s happened recently and what’s happening now, and you can do this with [5 commands](https://www.linux.com/training-tutorials/first-5-commands-when-i-connect-linux-server/) in a minute or less:

## W
- shows server [uptime](https://www.techtarget.com/whatis/definition/uptime-and-downtime)  which is the time during which the server has been continuously running
- shows which users are connected to the server
- load average will give you a good sense of the server health - (read more about load [here](https://scoutapm.com/blog/understanding-load-averages) and [here](https://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html))

## history

- shows which commands were previously run by the user you are currently connected to
- you can learn a lot about what type of work was previously performed on the machine, and what could have gone wrong with it
- where you might want to start your debugging work

## top

- shows what is currently running on this server
- order results by CPU, memory utilization and catch the ones that are resource intensive
