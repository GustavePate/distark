### add a service

#####  goto ressources/commons/protos/service
* create a new file
* define request and response following conventions 

##### goto ressources/commons/protos/generic_service.proto
* add import to the new service.proto
* add response to OneResponse
* add request to OneRequest
* add entry to RequestType enum
* add entry to ResponseType enum
* make protoc

##### goto src/distark/majordaemon/client/services
* create a servicenameservice.py must contain:
* a ServicenameRequest class (must implement fillinPBOneRequest(self, pbonereq): )
* a ServicenameResponse class (must map its fields with a OneResponse in __init__)
* a ServicenameService class (register associated response type, response handler and send)

##### goto src/distark/majordaemon/client/test
* create a test_servicenameservice.py must contain:
* a TestServiceNameService class
* with a test_servicenameservice method marked as fullstack

##### goto src/distark/majordaemon/client/worker/processor
* create a servicenameprocessor.py must contain:
* an __init__ method which store a PBServicenameRequest
* a process method which return a PBServicenameResponse

##### goto src/distark/majordaemon/client/worker/mdworker.py
* import processor, request & response type
* add a servicename_request method which take a pbonerequest in and returns a pboneresponse
* add the mapping request_type / handler in the existing_services dic of handle_request

make test
Done!
