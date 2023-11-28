#Conn: {
    address:  string
    port:     int
    protocol: string
    // ...    // uncomment this to allow any field
}

lossy: #Conn & {
    address:  "1.2.3.4"
    port:     8888
    protocol: "udp"
    // foo: 2 // uncomment this to get an error
}