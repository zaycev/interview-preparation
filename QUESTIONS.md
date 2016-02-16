# Questions

> DBMS, NoSQL, Scalability

* Read/Write ratio ­ Think about that.
    * How many reads compared to writes. For eg: Twitter has >100:1 ­ Random
seeks will be expensive! Distributed memcache? [with today’s tweets]?

* ACID requirements
    * Atomicity ­ Transactions are either completed on success or reverted on failure
    * Consistency ­ state is valid once transaction is over.
    * Isolation ­ Only one transaction can run at a time
    * Durability ­ Failover. State is maintained even in case of failover

* Memcache v/s Redis?
    * Memory cache is super popular. Basic in memory key value store
    * Redis cache ­ Distributed nicely, optional commit, larger object size. Supported in all major cloud environments.

* Sharding / Partitioning the database
    * Horizontal partitioning of table rows based on shard key
    * These shards can be split across multiple logical or physical servers
    * Indexes are fast and small over each shard.
    * Complex and single failure if there is no custom replication done of each
shard.

* Maintenance is hard
    * Data warehouse (Offline) ­ Syncs every x days with the main operation database with data denormalized into format needed for reporting. Can be wiped clean after Y days

* Primary / Secondary ­ Data redundancy. Active active is readable so can be used to reduce workloads. Geo redundancy ­ Minimum downtime

* Read/Write? Insert only vs locks?

* Pub/Sub channel. Topic based, content based.

* Throttling ­ Queues (worker service throttling)

* Flighting and A/B testing (Router based) ­ Deployment to a cluster and traffic manager handles that or Feature switch based. Out of band config deployment.

* CAP theorem ­ Consistency, Availability and Partition tolerance ­ chose 2.


*ASYNC EVERYWHERE, CACHES, SHARDING and CDN*

### References

* [1] Scaling Uber's Real-time Market Platform. [www.infoq.com](http://www.infoq.com/presentations/uber-market-platform)
* [2] How Uber Scales Their Real-Time Market Platform. [highscalability.com](http://highscalability.com/blog/2015/9/14/how-uber-scales-their-real-time-market-platform.html)
* [3] How We've Scaled Dropbox. [www.youtube.com](https://www.youtube.com/watch?v=PE4gwstWhmc)
* [4] Scaling Uber [www.infoq.com](http://www.infoq.com/presentations/uber-scalability-arch)
* [5] Stream Processing in Uber [www.infoq.com](http://www.infoq.com/presentations/uber-stream-processing)
* [6] Spark and Spark Streaming at Uber [www.youtube.com](https://www.youtube.com/watch?v=zKbds9ZPjLE&t=748)
