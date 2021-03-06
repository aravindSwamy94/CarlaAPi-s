# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prediction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='prediction.proto',
  package='',
  serialized_pb=_b('\n\x10prediction.proto\"\x87\x01\n\tPathPoint\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\r\n\x05theta\x18\x04 \x01(\x01\x12\r\n\x05kappa\x18\x05 \x01(\x01\x12\t\n\x01s\x18\x06 \x01(\x01\x12\x0e\n\x06\x64kappa\x18\x07 \x01(\x01\x12\x0f\n\x07\x64\x64kappa\x18\x08 \x01(\x01\x12\x0f\n\x07lane_id\x18\t \x01(\x05\"^\n\x0fTrajectoryPoint\x12\x1e\n\npath_point\x18\x01 \x01(\x0b\x32\n.PathPoint\x12\t\n\x01v\x18\x02 \x01(\x01\x12\t\n\x01\x61\x18\x03 \x01(\x01\x12\x15\n\rrelative_time\x18\x04 \x01(\x01\"M\n\nTrajectory\x12\x13\n\x0bprobability\x18\x01 \x01(\x01\x12*\n\x10trajectory_point\x18\x02 \x03(\x0b\x32\x10.TrajectoryPoint\"(\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\"\xd6\x04\n\x12PerceptionObstacle\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x18\n\x08position\x18\x02 \x01(\x0b\x32\x06.Point\x12\r\n\x05theta\x18\x03 \x01(\x01\x12\x18\n\x08velocity\x18\x04 \x01(\x0b\x32\x06.Point\x12\x0e\n\x06length\x18\x05 \x01(\x01\x12\r\n\x05width\x18\x06 \x01(\x01\x12\x0e\n\x06height\x18\x07 \x01(\x01\x12\x1d\n\rpolygon_point\x18\x08 \x03(\x0b\x32\x06.Point\x12\x15\n\rtracking_time\x18\t \x01(\x01\x12&\n\x04type\x18\n \x01(\x0e\x32\x18.PerceptionObstacle.Type\x12\x11\n\ttimestamp\x18\x0b \x01(\x01\x12\x17\n\x0bpoint_cloud\x18\x0c \x03(\x01\x42\x02\x10\x01\x12\x15\n\nconfidence\x18\r \x01(\x01:\x01\x31\x12K\n\x0f\x63onfidence_type\x18\x0e \x01(\x0e\x32\".PerceptionObstacle.ConfidenceType:\x0e\x43ONFIDENCE_CNN\x12\x15\n\x05\x64rops\x18\x0f \x03(\x0b\x32\x06.Point\"i\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x13\n\x0fUNKNOWN_MOVABLE\x10\x01\x12\x15\n\x11UNKNOWN_UNMOVABLE\x10\x02\x12\x0e\n\nPEDESTRIAN\x10\x03\x12\x0b\n\x07\x42ICYCLE\x10\x04\x12\x0b\n\x07VEHICLE\x10\x05\"R\n\x0e\x43onfidenceType\x12\x16\n\x12\x43ONFIDENCE_UNKNOWN\x10\x00\x12\x12\n\x0e\x43ONFIDENCE_CNN\x10\x01\x12\x14\n\x10\x43ONFIDENCE_RADAR\x10\x02\"\x94\x01\n\x12PredictionObstacle\x12\x30\n\x13perception_obstacle\x18\x01 \x01(\x0b\x32\x13.PerceptionObstacle\x12\x11\n\ttimestamp\x18\x02 \x01(\x01\x12\x18\n\x10predicted_period\x18\x03 \x01(\x01\x12\x1f\n\ntrajectory\x18\x04 \x03(\x0b\x32\x0b.Trajectory\"w\n\x13PredictionObstacles\x12\x30\n\x13prediction_obstacle\x18\x02 \x03(\x0b\x32\x13.PredictionObstacle\x12\x17\n\x0fstart_timestamp\x18\x04 \x01(\x01\x12\x15\n\rend_timestamp\x18\x05 \x01(\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PERCEPTIONOBSTACLE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='PerceptionObstacle.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_MOVABLE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_UNMOVABLE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PEDESTRIAN', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BICYCLE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VEHICLE', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=785,
  serialized_end=890,
)
_sym_db.RegisterEnumDescriptor(_PERCEPTIONOBSTACLE_TYPE)

_PERCEPTIONOBSTACLE_CONFIDENCETYPE = _descriptor.EnumDescriptor(
  name='ConfidenceType',
  full_name='PerceptionObstacle.ConfidenceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONFIDENCE_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIDENCE_CNN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIDENCE_RADAR', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=892,
  serialized_end=974,
)
_sym_db.RegisterEnumDescriptor(_PERCEPTIONOBSTACLE_CONFIDENCETYPE)


_PATHPOINT = _descriptor.Descriptor(
  name='PathPoint',
  full_name='PathPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='PathPoint.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='PathPoint.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='PathPoint.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='theta', full_name='PathPoint.theta', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kappa', full_name='PathPoint.kappa', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='s', full_name='PathPoint.s', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dkappa', full_name='PathPoint.dkappa', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ddkappa', full_name='PathPoint.ddkappa', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lane_id', full_name='PathPoint.lane_id', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=156,
)


_TRAJECTORYPOINT = _descriptor.Descriptor(
  name='TrajectoryPoint',
  full_name='TrajectoryPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path_point', full_name='TrajectoryPoint.path_point', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='v', full_name='TrajectoryPoint.v', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='a', full_name='TrajectoryPoint.a', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relative_time', full_name='TrajectoryPoint.relative_time', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=252,
)


_TRAJECTORY = _descriptor.Descriptor(
  name='Trajectory',
  full_name='Trajectory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='probability', full_name='Trajectory.probability', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trajectory_point', full_name='Trajectory.trajectory_point', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=254,
  serialized_end=331,
)


_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='Point.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='Point.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='Point.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=333,
  serialized_end=373,
)


_PERCEPTIONOBSTACLE = _descriptor.Descriptor(
  name='PerceptionObstacle',
  full_name='PerceptionObstacle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PerceptionObstacle.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='PerceptionObstacle.position', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='theta', full_name='PerceptionObstacle.theta', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='PerceptionObstacle.velocity', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='length', full_name='PerceptionObstacle.length', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='PerceptionObstacle.width', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='PerceptionObstacle.height', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='polygon_point', full_name='PerceptionObstacle.polygon_point', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tracking_time', full_name='PerceptionObstacle.tracking_time', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='PerceptionObstacle.type', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='PerceptionObstacle.timestamp', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point_cloud', full_name='PerceptionObstacle.point_cloud', index=11,
      number=12, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='PerceptionObstacle.confidence', index=12,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confidence_type', full_name='PerceptionObstacle.confidence_type', index=13,
      number=14, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drops', full_name='PerceptionObstacle.drops', index=14,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PERCEPTIONOBSTACLE_TYPE,
    _PERCEPTIONOBSTACLE_CONFIDENCETYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=376,
  serialized_end=974,
)


_PREDICTIONOBSTACLE = _descriptor.Descriptor(
  name='PredictionObstacle',
  full_name='PredictionObstacle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='perception_obstacle', full_name='PredictionObstacle.perception_obstacle', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='PredictionObstacle.timestamp', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predicted_period', full_name='PredictionObstacle.predicted_period', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trajectory', full_name='PredictionObstacle.trajectory', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=977,
  serialized_end=1125,
)


_PREDICTIONOBSTACLES = _descriptor.Descriptor(
  name='PredictionObstacles',
  full_name='PredictionObstacles',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prediction_obstacle', full_name='PredictionObstacles.prediction_obstacle', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_timestamp', full_name='PredictionObstacles.start_timestamp', index=1,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_timestamp', full_name='PredictionObstacles.end_timestamp', index=2,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1127,
  serialized_end=1246,
)

_TRAJECTORYPOINT.fields_by_name['path_point'].message_type = _PATHPOINT
_TRAJECTORY.fields_by_name['trajectory_point'].message_type = _TRAJECTORYPOINT
_PERCEPTIONOBSTACLE.fields_by_name['position'].message_type = _POINT
_PERCEPTIONOBSTACLE.fields_by_name['velocity'].message_type = _POINT
_PERCEPTIONOBSTACLE.fields_by_name['polygon_point'].message_type = _POINT
_PERCEPTIONOBSTACLE.fields_by_name['type'].enum_type = _PERCEPTIONOBSTACLE_TYPE
_PERCEPTIONOBSTACLE.fields_by_name['confidence_type'].enum_type = _PERCEPTIONOBSTACLE_CONFIDENCETYPE
_PERCEPTIONOBSTACLE.fields_by_name['drops'].message_type = _POINT
_PERCEPTIONOBSTACLE_TYPE.containing_type = _PERCEPTIONOBSTACLE
_PERCEPTIONOBSTACLE_CONFIDENCETYPE.containing_type = _PERCEPTIONOBSTACLE
_PREDICTIONOBSTACLE.fields_by_name['perception_obstacle'].message_type = _PERCEPTIONOBSTACLE
_PREDICTIONOBSTACLE.fields_by_name['trajectory'].message_type = _TRAJECTORY
_PREDICTIONOBSTACLES.fields_by_name['prediction_obstacle'].message_type = _PREDICTIONOBSTACLE
DESCRIPTOR.message_types_by_name['PathPoint'] = _PATHPOINT
DESCRIPTOR.message_types_by_name['TrajectoryPoint'] = _TRAJECTORYPOINT
DESCRIPTOR.message_types_by_name['Trajectory'] = _TRAJECTORY
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['PerceptionObstacle'] = _PERCEPTIONOBSTACLE
DESCRIPTOR.message_types_by_name['PredictionObstacle'] = _PREDICTIONOBSTACLE
DESCRIPTOR.message_types_by_name['PredictionObstacles'] = _PREDICTIONOBSTACLES

PathPoint = _reflection.GeneratedProtocolMessageType('PathPoint', (_message.Message,), dict(
  DESCRIPTOR = _PATHPOINT,
  __module__ = 'prediction_pb2'
  # @@protoc_insertion_point(class_scope:PathPoint)
  ))
_sym_db.RegisterMessage(PathPoint)

TrajectoryPoint = _reflection.GeneratedProtocolMessageType('TrajectoryPoint', (_message.Message,), dict(
  DESCRIPTOR = _TRAJECTORYPOINT,
  __module__ = 'prediction_pb2'
  # @@protoc_insertion_point(class_scope:TrajectoryPoint)
  ))
_sym_db.RegisterMessage(TrajectoryPoint)

Trajectory = _reflection.GeneratedProtocolMessageType('Trajectory', (_message.Message,), dict(
  DESCRIPTOR = _TRAJECTORY,
  __module__ = 'prediction_pb2'
  # @@protoc_insertion_point(class_scope:Trajectory)
  ))
_sym_db.RegisterMessage(Trajectory)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), dict(
  DESCRIPTOR = _POINT,
  __module__ = 'prediction_pb2'
  # @@protoc_insertion_point(class_scope:Point)
  ))
_sym_db.RegisterMessage(Point)

PerceptionObstacle = _reflection.GeneratedProtocolMessageType('PerceptionObstacle', (_message.Message,), dict(
  DESCRIPTOR = _PERCEPTIONOBSTACLE,
  __module__ = 'prediction_pb2'
  # @@protoc_insertion_point(class_scope:PerceptionObstacle)
  ))
_sym_db.RegisterMessage(PerceptionObstacle)

PredictionObstacle = _reflection.GeneratedProtocolMessageType('PredictionObstacle', (_message.Message,), dict(
  DESCRIPTOR = _PREDICTIONOBSTACLE,
  __module__ = 'prediction_pb2'
  # @@protoc_insertion_point(class_scope:PredictionObstacle)
  ))
_sym_db.RegisterMessage(PredictionObstacle)

PredictionObstacles = _reflection.GeneratedProtocolMessageType('PredictionObstacles', (_message.Message,), dict(
  DESCRIPTOR = _PREDICTIONOBSTACLES,
  __module__ = 'prediction_pb2'
  # @@protoc_insertion_point(class_scope:PredictionObstacles)
  ))
_sym_db.RegisterMessage(PredictionObstacles)


_PERCEPTIONOBSTACLE.fields_by_name['point_cloud'].has_options = True
_PERCEPTIONOBSTACLE.fields_by_name['point_cloud']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
