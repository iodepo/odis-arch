#LoggingLinuxVM: {
  resource_id:  #NonEmptyString
  version:      =~"2020-07-21"
  type:         =~"Linux"
  properties:   #LoggingPropertiesLinuxVM
}

#LoggingPropertiesLinuxVM: {
  CustomLogFiles: [...#NonEmptyString]
}

#NonEmptyString: string & !=""
