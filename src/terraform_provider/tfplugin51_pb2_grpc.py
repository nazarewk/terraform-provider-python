# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from terraform_provider import tfplugin51_pb2 as terraform__provider_dot_tfplugin51__pb2


class ProviderStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetSchema = channel.unary_unary(
        '/tfplugin5.Provider/GetSchema',
        request_serializer=terraform__provider_dot_tfplugin51__pb2.GetProviderSchema.Request.SerializeToString,
        response_deserializer=terraform__provider_dot_tfplugin51__pb2.GetProviderSchema.Response.FromString,
        )
    self.PrepareProviderConfig = channel.unary_unary(
        '/tfplugin5.Provider/PrepareProviderConfig',
        request_serializer=terraform__provider_dot_tfplugin51__pb2.PrepareProviderConfig.Request.SerializeToString,
        response_deserializer=terraform__provider_dot_tfplugin51__pb2.PrepareProviderConfig.Response.FromString,
        )
    self.ValidateResourceTypeConfig = channel.unary_unary(
        '/tfplugin5.Provider/ValidateResourceTypeConfig',
        request_serializer=terraform__provider_dot_tfplugin51__pb2.ValidateResourceTypeConfig.Request.SerializeToString,
        response_deserializer=terraform__provider_dot_tfplugin51__pb2.ValidateResourceTypeConfig.Response.FromString,
        )
    self.ValidateDataSourceConfig = channel.unary_unary(
        '/tfplugin5.Provider/ValidateDataSourceConfig',
        request_serializer=terraform__provider_dot_tfplugin51__pb2.ValidateDataSourceConfig.Request.SerializeToString,
        response_deserializer=terraform__provider_dot_tfplugin51__pb2.ValidateDataSourceConfig.Response.FromString,
        )
    self.UpgradeResourceState = channel.unary_unary(
        '/tfplugin5.Provider/UpgradeResourceState',
        request_serializer=terraform__provider_dot_tfplugin51__pb2.UpgradeResourceState.Request.SerializeToString,
        response_deserializer=terraform__provider_dot_tfplugin51__pb2.UpgradeResourceState.Response.FromString,
        )
    self.Configure = channel.unary_unary(
        '/tfplugin5.Provider/Configure',
        request_serializer=terraform__provider_dot_tfplugin51__pb2.Configure.Request.SerializeToString,
        response_deserializer=terraform__provider_dot_tfplugin51__pb2.Configure.Response.FromString,
        )
    self.ReadResource = channel.unary_unary(
        '/tfplugin5.Provider/ReadResource',
        request_serializer=terraform__provider_dot_tfplugin51__pb2.ReadResource.Request.SerializeToString,
        response_deserializer=terraform__provider_dot_tfplugin51__pb2.ReadResource.Response.FromString,
        )
    self.PlanResourceChange = channel.unary_unary(
        '/tfplugin5.Provider/PlanResourceChange',
        request_serializer=terraform__provider_dot_tfplugin51__pb2.PlanResourceChange.Request.SerializeToString,
        response_deserializer=terraform__provider_dot_tfplugin51__pb2.PlanResourceChange.Response.FromString,
        )
    self.ApplyResourceChange = channel.unary_unary(
        '/tfplugin5.Provider/ApplyResourceChange',
        request_serializer=terraform__provider_dot_tfplugin51__pb2.ApplyResourceChange.Request.SerializeToString,
        response_deserializer=terraform__provider_dot_tfplugin51__pb2.ApplyResourceChange.Response.FromString,
        )
    self.ImportResourceState = channel.unary_unary(
        '/tfplugin5.Provider/ImportResourceState',
        request_serializer=terraform__provider_dot_tfplugin51__pb2.ImportResourceState.Request.SerializeToString,
        response_deserializer=terraform__provider_dot_tfplugin51__pb2.ImportResourceState.Response.FromString,
        )
    self.ReadDataSource = channel.unary_unary(
        '/tfplugin5.Provider/ReadDataSource',
        request_serializer=terraform__provider_dot_tfplugin51__pb2.ReadDataSource.Request.SerializeToString,
        response_deserializer=terraform__provider_dot_tfplugin51__pb2.ReadDataSource.Response.FromString,
        )
    self.Stop = channel.unary_unary(
        '/tfplugin5.Provider/Stop',
        request_serializer=terraform__provider_dot_tfplugin51__pb2.Stop.Request.SerializeToString,
        response_deserializer=terraform__provider_dot_tfplugin51__pb2.Stop.Response.FromString,
        )


class ProviderServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetSchema(self, request, context):
    """////// Information about what a provider supports/expects
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PrepareProviderConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ValidateResourceTypeConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ValidateDataSourceConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpgradeResourceState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Configure(self, request, context):
    """////// One-time initialization, called before other functions below
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadResource(self, request, context):
    """////// Managed Resource Lifecycle
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PlanResourceChange(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ApplyResourceChange(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ImportResourceState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadDataSource(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Stop(self, request, context):
    """////// Graceful Shutdown
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ProviderServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetSchema': grpc.unary_unary_rpc_method_handler(
          servicer.GetSchema,
          request_deserializer=terraform__provider_dot_tfplugin51__pb2.GetProviderSchema.Request.FromString,
          response_serializer=terraform__provider_dot_tfplugin51__pb2.GetProviderSchema.Response.SerializeToString,
      ),
      'PrepareProviderConfig': grpc.unary_unary_rpc_method_handler(
          servicer.PrepareProviderConfig,
          request_deserializer=terraform__provider_dot_tfplugin51__pb2.PrepareProviderConfig.Request.FromString,
          response_serializer=terraform__provider_dot_tfplugin51__pb2.PrepareProviderConfig.Response.SerializeToString,
      ),
      'ValidateResourceTypeConfig': grpc.unary_unary_rpc_method_handler(
          servicer.ValidateResourceTypeConfig,
          request_deserializer=terraform__provider_dot_tfplugin51__pb2.ValidateResourceTypeConfig.Request.FromString,
          response_serializer=terraform__provider_dot_tfplugin51__pb2.ValidateResourceTypeConfig.Response.SerializeToString,
      ),
      'ValidateDataSourceConfig': grpc.unary_unary_rpc_method_handler(
          servicer.ValidateDataSourceConfig,
          request_deserializer=terraform__provider_dot_tfplugin51__pb2.ValidateDataSourceConfig.Request.FromString,
          response_serializer=terraform__provider_dot_tfplugin51__pb2.ValidateDataSourceConfig.Response.SerializeToString,
      ),
      'UpgradeResourceState': grpc.unary_unary_rpc_method_handler(
          servicer.UpgradeResourceState,
          request_deserializer=terraform__provider_dot_tfplugin51__pb2.UpgradeResourceState.Request.FromString,
          response_serializer=terraform__provider_dot_tfplugin51__pb2.UpgradeResourceState.Response.SerializeToString,
      ),
      'Configure': grpc.unary_unary_rpc_method_handler(
          servicer.Configure,
          request_deserializer=terraform__provider_dot_tfplugin51__pb2.Configure.Request.FromString,
          response_serializer=terraform__provider_dot_tfplugin51__pb2.Configure.Response.SerializeToString,
      ),
      'ReadResource': grpc.unary_unary_rpc_method_handler(
          servicer.ReadResource,
          request_deserializer=terraform__provider_dot_tfplugin51__pb2.ReadResource.Request.FromString,
          response_serializer=terraform__provider_dot_tfplugin51__pb2.ReadResource.Response.SerializeToString,
      ),
      'PlanResourceChange': grpc.unary_unary_rpc_method_handler(
          servicer.PlanResourceChange,
          request_deserializer=terraform__provider_dot_tfplugin51__pb2.PlanResourceChange.Request.FromString,
          response_serializer=terraform__provider_dot_tfplugin51__pb2.PlanResourceChange.Response.SerializeToString,
      ),
      'ApplyResourceChange': grpc.unary_unary_rpc_method_handler(
          servicer.ApplyResourceChange,
          request_deserializer=terraform__provider_dot_tfplugin51__pb2.ApplyResourceChange.Request.FromString,
          response_serializer=terraform__provider_dot_tfplugin51__pb2.ApplyResourceChange.Response.SerializeToString,
      ),
      'ImportResourceState': grpc.unary_unary_rpc_method_handler(
          servicer.ImportResourceState,
          request_deserializer=terraform__provider_dot_tfplugin51__pb2.ImportResourceState.Request.FromString,
          response_serializer=terraform__provider_dot_tfplugin51__pb2.ImportResourceState.Response.SerializeToString,
      ),
      'ReadDataSource': grpc.unary_unary_rpc_method_handler(
          servicer.ReadDataSource,
          request_deserializer=terraform__provider_dot_tfplugin51__pb2.ReadDataSource.Request.FromString,
          response_serializer=terraform__provider_dot_tfplugin51__pb2.ReadDataSource.Response.SerializeToString,
      ),
      'Stop': grpc.unary_unary_rpc_method_handler(
          servicer.Stop,
          request_deserializer=terraform__provider_dot_tfplugin51__pb2.Stop.Request.FromString,
          response_serializer=terraform__provider_dot_tfplugin51__pb2.Stop.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'tfplugin5.Provider', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class ProvisionerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetSchema = channel.unary_unary(
        '/tfplugin5.Provisioner/GetSchema',
        request_serializer=terraform__provider_dot_tfplugin51__pb2.GetProvisionerSchema.Request.SerializeToString,
        response_deserializer=terraform__provider_dot_tfplugin51__pb2.GetProvisionerSchema.Response.FromString,
        )
    self.ValidateProvisionerConfig = channel.unary_unary(
        '/tfplugin5.Provisioner/ValidateProvisionerConfig',
        request_serializer=terraform__provider_dot_tfplugin51__pb2.ValidateProvisionerConfig.Request.SerializeToString,
        response_deserializer=terraform__provider_dot_tfplugin51__pb2.ValidateProvisionerConfig.Response.FromString,
        )
    self.ProvisionResource = channel.unary_stream(
        '/tfplugin5.Provisioner/ProvisionResource',
        request_serializer=terraform__provider_dot_tfplugin51__pb2.ProvisionResource.Request.SerializeToString,
        response_deserializer=terraform__provider_dot_tfplugin51__pb2.ProvisionResource.Response.FromString,
        )
    self.Stop = channel.unary_unary(
        '/tfplugin5.Provisioner/Stop',
        request_serializer=terraform__provider_dot_tfplugin51__pb2.Stop.Request.SerializeToString,
        response_deserializer=terraform__provider_dot_tfplugin51__pb2.Stop.Response.FromString,
        )


class ProvisionerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetSchema(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ValidateProvisionerConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ProvisionResource(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Stop(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ProvisionerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetSchema': grpc.unary_unary_rpc_method_handler(
          servicer.GetSchema,
          request_deserializer=terraform__provider_dot_tfplugin51__pb2.GetProvisionerSchema.Request.FromString,
          response_serializer=terraform__provider_dot_tfplugin51__pb2.GetProvisionerSchema.Response.SerializeToString,
      ),
      'ValidateProvisionerConfig': grpc.unary_unary_rpc_method_handler(
          servicer.ValidateProvisionerConfig,
          request_deserializer=terraform__provider_dot_tfplugin51__pb2.ValidateProvisionerConfig.Request.FromString,
          response_serializer=terraform__provider_dot_tfplugin51__pb2.ValidateProvisionerConfig.Response.SerializeToString,
      ),
      'ProvisionResource': grpc.unary_stream_rpc_method_handler(
          servicer.ProvisionResource,
          request_deserializer=terraform__provider_dot_tfplugin51__pb2.ProvisionResource.Request.FromString,
          response_serializer=terraform__provider_dot_tfplugin51__pb2.ProvisionResource.Response.SerializeToString,
      ),
      'Stop': grpc.unary_unary_rpc_method_handler(
          servicer.Stop,
          request_deserializer=terraform__provider_dot_tfplugin51__pb2.Stop.Request.FromString,
          response_serializer=terraform__provider_dot_tfplugin51__pb2.Stop.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'tfplugin5.Provisioner', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
