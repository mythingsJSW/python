import math
import struct
import os

def save_to_ply(point_cloud, filename="point_cloud.ply"):
    """
    PLY 파일로 포인트 클라우드를 저장하며, 파일 이름이 이미 존재하면 자동으로 번호를 증가시켜 저장합니다.
    """
    # 파일 이름 중복 방지 - point_cloud_n.ply 형식으로 저장
    base_filename, extension = os.path.splitext(filename)
    count = 1
    new_filename = filename

    while os.path.exists(new_filename):
        new_filename = f"{base_filename}_{count}{extension}"
        count += 1

    # PLY 파일 헤더 작성
    header = f"""ply
format ascii 1.0
element vertex {len(point_cloud)}
property float x
property float y
property float z
property float intensity
end_header
"""

    # 포인트 데이터를 헤더와 함께 파일에 작성
    with open(new_filename, 'w') as ply_file:
        ply_file.write(header)
        for x, y, z, intensity in point_cloud:
            ply_file.write(f"{x} {y} {z} {float(intensity)}\n")

    print(f"PLY 파일이 생성되었습니다: {new_filename}")


def coordinate(data):

    # 데이터 길이 검사
    if len(data) < 25:  # 헤더 길이만큼 검사
        print("Error: 데이터 길이가 너무 짧습니다.")
        return

    # 헤더 디코딩
    timestamp, measurement_id, num_results, trigger_counter = struct.unpack("<QIIi", data[16:36])
    time_scale = 1e-16
    z_val = timestamp * time_scale
    x_value=[]
    y_value=[]
    angle_list=[]
    # 채널별 데이터 처리
    offset = 20
    while offset < len(data) -8:
        # 각 채널 데이터 디코딩 (Range, Phi, Intensity)
        range_value, phi_value, intensity_value = struct.unpack("<IHH", data[offset:offset + 8])
        range_meters = range_value * 0.0001  # 0.1mm 단위 -> 미터
        phi_degrees = phi_value * 0.001  # 1/1000도 단위 -> 도
        # 거리값이 유효하지 않으면 스킵
        if range_meters == 0:
            offset += 8
            continue

        # Phi 각도를 라디안으로 변환
        #phi_radians = math.radians(phi_degrees)

        # 3D 좌표 변환
        #x = range_meters #* math.cos(math.radians(phi_degrees))
        x = range_meters * math.sin(math.radians(90.0-phi_degrees))
        x_value.append(x)
        angle_list.append(phi_degrees)
        # 다음 채널로 이동
        offset += 8

    # 노멀라이제이션
    # 1. y_value 계산
    y_value = []
    for x, angle in zip(x_value, angle_list):

        #y = -x * math.sin(math.radians(angle))
        y = -x * math.cos(math.radians(90.0-angle))
        y_value.append(y)
    #y_value = [-k for k in y_value]
    return x_value, y_value