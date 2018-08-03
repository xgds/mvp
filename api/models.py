from mongoengine import *


class Header(Document):    
    stamp = DateTimeField()
    frame_id = StringField()


class GoalID(Document):    
    stamp = DateTimeField()


class MultiArrayDimension(Document):    
    label = StringField()
    size = IntField()
    stride = IntField()


class KeyValue(Document):    
    key = StringField()
    value = StringField()


class DiagnosticStatus(Document):    
    OK = 0
    WARN = 1
    ERROR = 2
    STALE = 3
    level = BinaryField()
    name = StringField()
    message = StringField()
    hardware_id = StringField()
    values = ListField(ReferenceField(KeyValue))


class MultiArrayLayout(Document):    
    dim = ListField(ReferenceField(MultiArrayDimension))
    data_offset = IntField()


class GoalStatus(Document):    
    goal_id = ReferenceField(GoalID)
    status = IntField()
    pending = IntField()
    active = IntField()
    preempted = IntField()
    succeeded = IntField()
    aborted = IntField()
    rejected = IntField()
    preempting = IntField()
    recalling = IntField()
    recalled = IntField()
    lost = IntField()
    text = StringField()


class GoalStatusArray(Document):    
    header = ReferenceField(Header)
    status_list = ListField(ReferenceField(GoalStatus))


class DiagnosticArray(Document):    
    header = ReferenceField(Header)
    status = ListField(ReferenceField(DiagnosticStatus))


class Vector3(Document):    
    x = FloatField()
    y = FloatField()
    z = FloatField()


class Accel(Document):    
    linear = ReferenceField(Vector3)
    angular = ReferenceField(Vector3)


class AccelStamped(Document):    
    header = ReferenceField(Header)
    accel = ReferenceField(Accel)


class AccelWithCovariance(Document):    
    accel = ReferenceField(Accel)
    covariance = ListField(FloatField())


class AccelWithCovarianceStamped(Document):    
    header = ReferenceField(Header)
    accel = ReferenceField(AccelWithCovariance)


class Inertia(Document):    
    m = FloatField()
    com = ReferenceField(Vector3)
    ixx = FloatField()
    ixy = FloatField()
    ixz = FloatField()
    iyy = FloatField()
    iyz = FloatField()
    izz = FloatField()


class InertiaStamped(Document):    
    header = ReferenceField(Header)
    inertia = ReferenceField(Inertia)


class Point(Document):    
    x = FloatField()
    y = FloatField()
    z = FloatField()


class Point32(Document):    
    x = FloatField()
    y = FloatField()
    z = FloatField()


class PointStamped(Document):    
    header = ReferenceField(Header)
    point = ReferenceField(Point)


class Polygon(Document):    
    points = ListField(ReferenceField(Point32))


class PolygonStamped(Document):    
    header = ReferenceField(Header)
    polygon = ReferenceField(Polygon)


class Quaternion(Document):    
    x = FloatField()
    y = FloatField()
    z = FloatField()
    w = FloatField()


class Pose(Document):    
    position = ReferenceField(Point)
    orientation = ReferenceField(Quaternion)


class Pose2D(Document):    
    x = FloatField()
    y = FloatField()
    theta = FloatField()


class PoseArray(Document):    
    header = ReferenceField(Header)
    poses = ListField(ReferenceField(Pose))


class PoseStamped(Document):    
    header = ReferenceField(Header)
    pose = ReferenceField(Pose)


class PoseWithCovariance(Document):    
    pose = ReferenceField(Pose)
    covariance = ListField(FloatField())


class PoseWithCovarianceStamped(Document):    
    header = ReferenceField(Header)
    pose = ReferenceField(PoseWithCovariance)


class QuaternionStamped(Document):    
    header = ReferenceField(Header)
    quaternion = ReferenceField(Quaternion)


class Transform(Document):    
    translation = ReferenceField(Vector3)
    rotation = ReferenceField(Quaternion)


class TransformStamped(Document):    
    header = ReferenceField(Header)
    child_frame_id = StringField()
    transform = ReferenceField(Transform)


class Twist(Document):    
    linear = ReferenceField(Vector3)
    angular = ReferenceField(Vector3)


class TwistStamped(Document):    
    header = ReferenceField(Header)
    twist = ReferenceField(Twist)


class TwistWithCovariance(Document):    
    twist = ReferenceField(Twist)
    covariance = ListField(FloatField())


class TwistWithCovarianceStamped(Document):    
    header = ReferenceField(Header)
    twist = ReferenceField(TwistWithCovariance)


class Vector3Stamped(Document):    
    header = ReferenceField(Header)
    vector = ReferenceField(Vector3)


class Wrench(Document):    
    force = ReferenceField(Vector3)
    torque = ReferenceField(Vector3)


class WrenchStamped(Document):    
    header = ReferenceField(Header)
    wrench = ReferenceField(Wrench)


class GridCells(Document):    
    header = ReferenceField(Header)
    cell_width = FloatField()
    cell_height = FloatField()
    cells = ListField(ReferenceField(Point))


class MapMetaData(Document):    
    map_load_time = DateTimeField()
    resolution = FloatField()
    width = IntField()
    height = IntField()
    origin = ReferenceField(Pose)


class OccupancyGrid(Document):    
    header = ReferenceField(Header)
    info = ReferenceField(MapMetaData)
    data = ListField(IntField())


class Odometry(Document):    
    header = ReferenceField(Header)
    child_frame_id = StringField()
    pose = ReferenceField(PoseWithCovariance)
    twist = ReferenceField(TwistWithCovariance)


class Path(Document):    
    header = ReferenceField(Header)
    poses = ListField(ReferenceField(PoseStamped))


class BatteryState(Document):    
    power_supply_status_unknown = IntField()
    power_supply_status_charging = IntField()
    power_supply_status_discharging = IntField()
    power_supply_status_not_charging = IntField()
    power_supply_status_full = IntField()
    power_supply_health_unknown = IntField()
    power_supply_health_good = IntField()
    power_supply_health_overheat = IntField()
    power_supply_health_dead = IntField()
    power_supply_health_overvoltage = IntField()
    power_supply_health_unspec_failure = IntField()
    power_supply_health_cold = IntField()
    power_supply_health_watchdog_timer_expire = IntField()
    power_supply_health_safety_timer_expire = IntField()
    power_supply_technology_unknown = IntField()
    power_supply_technology_nimh = IntField()
    power_supply_technology_lion = IntField()
    power_supply_technology_lipo = IntField()
    power_supply_technology_life = IntField()
    power_supply_technology_nicd = IntField()
    power_supply_technology_limn = IntField()
    header = ReferenceField(Header)
    voltage = FloatField()
    current = FloatField()
    charge = FloatField()
    capacity = FloatField()
    design_capacity = FloatField()
    percentage = FloatField()
    power_supply_status = IntField()
    power_supply_health = IntField()
    power_supply_technology = IntField()
    present = BooleanField()
    cell_voltage = ListField(FloatField())
    location = StringField()
    serial_number = StringField()


class RegionOfInterest(Document):    
    x_offset = IntField()
    y_offset = IntField()
    height = IntField()
    width = IntField()
    do_rectify = BooleanField()


class CameraInfo(Document):    
    header = ReferenceField(Header)
    height = IntField()
    width = IntField()
    distortion_model = StringField()
    d = ListField(FloatField())
    k = ListField(FloatField())
    r = ListField(FloatField())
    p = ListField(FloatField())
    binning_x = IntField()
    binning_y = IntField()
    roi = ReferenceField(RegionOfInterest)


class ChannelFloat32(Document):    
    name = StringField()
    values = ListField(FloatField())


class CompressedImage(Document):    
    header = ReferenceField(Header)
    format = StringField()
    data = ListField(IntField())


class FluidPressure(Document):    
    header = ReferenceField(Header)
    fluid_pressure = FloatField()
    variance = FloatField()


class Illuminance(Document):    
    header = ReferenceField(Header)
    illuminance = FloatField()
    variance = FloatField()


class Image(Document):    
    header = ReferenceField(Header)
    height = IntField()
    width = IntField()
    encoding = StringField()
    is_bigendian = IntField()
    step = IntField()
    data = ListField(IntField())


class Imu(Document):    
    header = ReferenceField(Header)
    orientation = ReferenceField(Quaternion)
    orientation_covariance = ListField(FloatField())
    angular_velocity = ReferenceField(Vector3)
    angular_velocity_covariance = ListField(FloatField())
    linear_acceleration = ReferenceField(Vector3)
    linear_acceleration_covariance = ListField(FloatField())


class JointState(Document):    
    header = ReferenceField(Header)
    name = ListField(StringField())
    position = ListField(FloatField())
    velocity = ListField(FloatField())
    effort = ListField(FloatField())


class Joy(Document):    
    header = ReferenceField(Header)
    axes = ListField(FloatField())
    buttons = ListField(IntField())


class JoyFeedback(Document):    
    type_led = IntField()
    type_rumble = IntField()
    type_buzzer = IntField()
    type = IntField()
    id = IntField()
    intensity = FloatField()


class JoyFeedbackArray(Document):    
    array = ListField(ReferenceField(JoyFeedback))


class LaserEcho(Document):    
    echoes = ListField(FloatField())


class LaserScan(Document):    
    header = ReferenceField(Header)
    angle_min = FloatField()
    angle_max = FloatField()
    angle_increment = FloatField()
    time_increment = FloatField()
    scan_time = FloatField()
    range_min = FloatField()
    range_max = FloatField()
    ranges = ListField(FloatField())
    intensities = ListField(FloatField())


class MagneticField(Document):    
    header = ReferenceField(Header)
    magnetic_field = ReferenceField(Vector3)
    magnetic_field_covariance = ListField(FloatField())


class MultiDOFJointState(Document):    
    header = ReferenceField(Header)
    joint_names = ListField(StringField())
    transforms = ListField(ReferenceField(Transform))
    twist = ListField(ReferenceField(Twist))
    wrench = ListField(ReferenceField(Wrench))


class MultiEchoLaserScan(Document):    
    header = ReferenceField(Header)
    angle_min = FloatField()
    angle_max = FloatField()
    angle_increment = FloatField()
    time_increment = FloatField()
    scan_time = FloatField()
    range_min = FloatField()
    range_max = FloatField()
    ranges = ListField(ReferenceField(LaserEcho))
    intensities = ListField(ReferenceField(LaserEcho))


class NavSatStatus(Document):    
    status_no_fix = IntField()
    status_fix = IntField()
    status_sbas_fix = IntField()
    status_gbas_fix = IntField()
    status = IntField()
    service_gps = IntField()
    service_glonass = IntField()
    service_compass = IntField()
    service_galileo = IntField()
    service = IntField()


class NavSatFix(Document):    
    header = ReferenceField(Header)
    status = ReferenceField(NavSatStatus)
    latitude = FloatField()
    longitude = FloatField()
    altitude = FloatField()
    position_covariance = ListField(FloatField())
    covariance_type_unknown = IntField()
    covariance_type_approximated = IntField()
    covariance_type_diagonal_known = IntField()
    covariance_type_known = IntField()
    position_covariance_type = IntField()


class PointCloud(Document):    
    header = ReferenceField(Header)
    points = ListField(ReferenceField(Point32))
    channels = ListField(ReferenceField(ChannelFloat32))


class PointField(Document):    
    int8 = IntField()
    uint8 = IntField()
    int16 = IntField()
    uint16 = IntField()
    int32 = IntField()
    uint32 = IntField()
    float32 = IntField()
    float64 = IntField()
    name = StringField()
    offset = IntField()
    datatype = IntField()
    count = IntField()


class PointCloud2(Document):    
    header = ReferenceField(Header)
    height = IntField()
    width = IntField()
    fields = ListField(ReferenceField(PointField))
    is_bigendian = BooleanField()
    point_step = IntField()
    row_step = IntField()
    data = ListField(IntField())
    is_dense = BooleanField()


class Range(Document):    
    header = ReferenceField(Header)
    ULTRASOUND = 0
    INFRARED = 1
    radiation_type = IntField()
    field_of_view = FloatField()
    min_range = FloatField()
    max_range = FloatField()
    range = FloatField()


class RelativeHumidity(Document):    
    header = ReferenceField(Header)
    relative_humidity = FloatField()
    variance = FloatField()


class Temperature(Document):    
    header = ReferenceField(Header)
    temperature = FloatField()
    variance = FloatField()


class TimeReference(Document):    
    header = ReferenceField(Header)
    time_ref = DateTimeField()
    source = StringField()


class MeshTriangle(Document):    
    vertex_indices = ListField(IntField())


class Mesh(Document):    
    triangles = ListField(ReferenceField(MeshTriangle))
    vertices = ListField(ReferenceField(Point))


class Plane(Document):    
    coef = ListField(FloatField())


class SolidPrimitive(Document):    
    BOX = 1
    SPHERE = 2
    CYLINDER = 3
    CONE = 4
    type = IntField()
    dimensions = ListField(FloatField())
    BOX_X = 0
    BOX_Y = 1
    BOX_Z = 2
    SPHERE_RADIUS = 0
    CYLINDER_HEIGHT = 0
    CYLINDER_RADIUS = 1
    CONE_HEIGHT = 0
    CONE_RADIUS = 1


class DisparityImage(Document):    
    header = ReferenceField(Header)
    image = ReferenceField(Image)
    f = FloatField()
    t = FloatField()
    valid_window = ReferenceField(RegionOfInterest)
    min_disparity = FloatField()
    max_disparity = FloatField()
    delta_d = FloatField()


class JointTrajectoryPoint(Document):    
    positions = ListField(FloatField())
    velocities = ListField(FloatField())
    accelerations = ListField(FloatField())
    effort = ListField(FloatField())
    time_from_start = IntField()


class JointTrajectory(Document):    
    header = ReferenceField(Header)
    joint_names = ListField(StringField())
    points = ListField(ReferenceField(JointTrajectoryPoint))


class MultiDOFJointTrajectoryPoint(Document):    
    transforms = ListField(ReferenceField(Transform))
    velocities = ListField(ReferenceField(Twist))
    accelerations = ListField(ReferenceField(Twist))
    time_from_start = IntField()


class MultiDOFJointTrajectory(Document):    
    header = ReferenceField(Header)
    joint_names = ListField(StringField())
    points = ListField(ReferenceField(MultiDOFJointTrajectoryPoint))


class ColorRGBA(Document):    
    r = FloatField()
    g = FloatField()
    b = FloatField()
    a = FloatField()


class ImageMarker(Document):    
    CIRCLE = 0
    LINE_STRIP = 1
    LINE_LIST = 2
    POLYGON = 3
    POINTS = 4
    ADD = 0
    REMOVE = 1
    header = ReferenceField(Header)
    ns = StringField()
    type = IntField()
    action = IntField()
    position = ReferenceField(Point)
    scale = FloatField()
    outline_color = ReferenceField(ColorRGBA)
    filled = IntField()
    fill_color = ReferenceField(ColorRGBA)
    lifetime = IntField()
    points = ListField(ReferenceField(Point))
    outline_colors = ListField(ReferenceField(ColorRGBA))


class Marker(Document):    
    ARROW = 0
    CUBE = 1
    SPHERE = 2
    CYLINDER = 3
    LINE_STRIP = 4
    LINE_LIST = 5
    CUBE_LIST = 6
    SPHERE_LIST = 7
    POINTS = 8
    TEXT_VIEW_FACING = 9
    MESH_RESOURCE = 10
    TRIANGLE_LIST = 11
    ADD = 0
    MODIFY = 0
    DELETE = 2
    DELETEALL = 3
    header = ReferenceField(Header)
    ns = StringField()
    type = IntField()
    action = IntField()
    pose = ReferenceField(Pose)
    scale = ReferenceField(Vector3)
    color = ReferenceField(ColorRGBA)
    lifetime = IntField()
    frame_locked = BooleanField()
    points = ListField(ReferenceField(Point))
    colors = ListField(ReferenceField(ColorRGBA))
    text = StringField()
    mesh_resource = StringField()
    mesh_use_embedded_materials = BooleanField()


class InteractiveMarkerControl(Document):    
    name = StringField()
    orientation = ReferenceField(Quaternion)
    inherit = IntField()
    fixed = IntField()
    view_facing = IntField()
    orientation_mode = IntField()
    none = IntField()
    menu = IntField()
    button = IntField()
    move_axis = IntField()
    move_plane = IntField()
    rotate_axis = IntField()
    move_rotate = IntField()
    move_3d = IntField()
    rotate_3d = IntField()
    move_rotate_3d = IntField()
    interaction_mode = IntField()
    always_visible = BooleanField()
    markers = ListField(ReferenceField(Marker))
    independent_marker_orientation = BooleanField()
    description = StringField()


class MenuEntry(Document):
    parent_id = IntField()
    title = StringField()
    command = StringField()
    FEEDBACK = 0
    ROSRUN = 1
    ROSLAUNCH = 2
    command_type = IntField()


class InteractiveMarker(Document):    
    header = ReferenceField(Header)
    pose = ReferenceField(Pose)
    name = StringField()
    description = StringField()
    scale = FloatField()
    menu_entries = ListField(ReferenceField(MenuEntry))
    controls = ListField(ReferenceField(InteractiveMarkerControl))


class InteractiveMarkerFeedback(Document):    
    header = ReferenceField(Header)
    client_id = StringField()
    marker_name = StringField()
    control_name = StringField()
    keep_alive = IntField()
    pose_update = IntField()
    menu_select = IntField()
    button_click = IntField()
    mouse_down = IntField()
    mouse_up = IntField()
    event_type = IntField()
    pose = ReferenceField(Pose)
    menu_entry_id = IntField()
    mouse_point = ReferenceField(Point)
    mouse_point_valid = BooleanField()


class InteractiveMarkerInit(Document):    
    server_id = StringField()
    seq_num = IntField()
    markers = ListField(ReferenceField(InteractiveMarker))


class InteractiveMarkerPose(Document):    
    header = ReferenceField(Header)
    pose = ReferenceField(Pose)
    name = StringField()


class InteractiveMarkerUpdate(Document):    
    server_id = StringField()
    seq_num = IntField()
    keep_alive = IntField()
    # update = IntField()
    type = IntField()
    markers = ListField(ReferenceField(InteractiveMarker))
    poses = ListField(ReferenceField(InteractiveMarkerPose))
    erases = ListField(StringField())


class MarkerArray(Document):    
    markers = ListField(ReferenceField(Marker))
