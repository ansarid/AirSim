# #!/usr/bin/python3

# # ready to run example: PythonClient/car/hello_car.py

# import airsim
# import time
# import gamepad

# controller = gamepad.Controller(0)

# # connect to the AirSim simulator
# client = airsim.CarClient()
# client.confirmConnection()
# client.enableApiControl(True)
# car_controls = airsim.CarControls()

# while True:

#     try:

#         button = controller.get_buttons()
#         joystick = controller.get_joysticks()
#         trigger = controller.get_triggers()

#         if controller.mode:

#             # print(button)
#             # print(joystick)
#             # print(trigger)

#             # get state of the car
#             car_state = client.getCarState()
#             print("Speed %d, Gear %d" % (car_state.speed, car_state.gear))

#             # set the controls for car
#             # car_controls.throttle = 1
#             car_controls.throttle = joystick['left']['y']
#             car_controls.steering = joystick['right']['x']
#             car_controls.brake = button['b']
#             car_controls.manual_gear = -1*button['a']

#             client.setCarControls(car_controls)

#             # # let car drive a bit
#             # time.sleep(1)

#             # # get camera images from the car
#             # responses = client.simGetImages([
#             #     airsim.ImageRequest(0, airsim.ImageType.DepthVis),
#             #     airsim.ImageRequest(1, airsim.ImageType.DepthPlanner, True)])
#             # print('Retrieved images: %d', len(responses))

#             # # do something with images
#             # for response in responses:
#             #     if response.pixels_as_float:
#             #         print("Type %d, size %d" % (response.image_type, len(response.image_data_float)))
#             #         airsim.write_pfm('py1.pfm', airsim.get_pfm_array(response))
#             #     else:
#             #         print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
#             #         airsim.write_file('py1.png', response.image_data_uint8)

#         else:

#             print("Error: Controller in incorrect mode!")
#             controller.reset()

#     except KeyboardInterrupt:
#         client.reset()
#         break

#     except Exception as e:
#         print(e)
#         client.reset()
#         break

















# import airsim
# import cv2
# import numpy as np
# import os
# import setup_path 
# import time

# # connect to the AirSim simulator 
# client = airsim.CarClient()
# client.confirmConnection()
# client.enableApiControl(True)
# car_controls = airsim.CarControls()

# while 1:
#     client.simSetWeatherParameter(airsim.WeatherParameter.Rain, 1);

# for idx in range(3):
#     # get state of the car
#     car_state = client.getCarState()
#     print("Speed %d, Gear %d" % (car_state.speed, car_state.gear))

#     # go forward
#     car_controls.throttle = 1
#     car_controls.steering = 0
#     client.setCarControls(car_controls)
#     print("Go Forward")
#     time.sleep(3)   # let car drive a bit

#     # Go forward + steer right
#     car_controls.throttle = 1
#     car_controls.steering = 1
#     client.setCarControls(car_controls)
#     print("Go Forward, steer right")
#     time.sleep(3)   # let car drive a bit

#     # go reverse
#     car_controls.throttle = -1
#     car_controls.is_manual_gear = True;
#     car_controls.manual_gear = -1
#     car_controls.steering = 0
#     client.setCarControls(car_controls)
#     print("Go reverse, steer right")
#     time.sleep(3)   # let car drive a bit
#     car_controls.is_manual_gear = False; # change back gear to auto
#     car_controls.manual_gear = 0  

#     # apply brakes
#     car_controls.brake = 1
#     client.setCarControls(car_controls)
#     print("Apply brakes")
#     time.sleep(3)   # let car drive a bit
#     car_controls.brake = 0 #remove brake

#     # # get camera images from the car
#     # responses = client.simGetImages([
#     #     airsim.ImageRequest("0", airsim.ImageType.DepthVis),  #depth visualization image
#     #     airsim.ImageRequest("1", airsim.ImageType.DepthPerspective, True), #depth in perspective projection
#     #     airsim.ImageRequest("1", airsim.ImageType.Scene), #scene vision image in png format
#     #     airsim.ImageRequest("1", airsim.ImageType.Scene, False, False)])  #scene vision image in uncompressed RGB array
#     # print('Retrieved images: %d', len(responses))

#     # for response in responses:
#     #     filename = 'c:/temp/py' + str(idx)
#     #     if not os.path.exists('c:/temp/'):
#     #         os.makedirs('c:/temp/')
#     #     if response.pixels_as_float:
#     #         print("Type %d, size %d" % (response.image_type, len(response.image_data_float)))
#     #         airsim.write_pfm(os.path.normpath(filename + '.pfm'), airsim.get_pfm_array(response))
#     #     elif response.compress: #png format
#     #         print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
#     #         airsim.write_file(os.path.normpath(filename + '.png'), response.image_data_uint8)
#     #     else: #uncompressed array
#     #         print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
#     #         img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8) # get numpy array
#     #         img_rgb = img1d.reshape(response.height, response.width, 3) # reshape array to 3 channel image array H X W X 3
#     #         cv2.imwrite(os.path.normpath(filename + '.png'), img_rgb) # write to png 

# #restore to original state
# client.reset()

# client.enableApiControl(False)

# import setup_path 
import airsim


client = airsim.VehicleClient()
client.confirmConnection()

client.simEnableWeather(True)

airsim.wait_key('Press any key to enable rain at 25%')
client.simSetWeatherParameter(airsim.WeatherParameter.Rain, 0.25);

airsim.wait_key('Press any key to enable rain at 75%')
client.simSetWeatherParameter(airsim.WeatherParameter.Rain, 0.75);

airsim.wait_key('Press any key to enable snow at 50%')
client.simSetWeatherParameter(airsim.WeatherParameter.Snow, 0.50);

airsim.wait_key('Press any key to enable maple leaves at 50%')
client.simSetWeatherParameter(airsim.WeatherParameter.MapleLeaf, 0.50);

airsim.wait_key('Press any key to set all effects to 0%')
client.simSetWeatherParameter(airsim.WeatherParameter.Rain, 0.0);
client.simSetWeatherParameter(airsim.WeatherParameter.Snow, 0.0);
client.simSetWeatherParameter(airsim.WeatherParameter.MapleLeaf, 0.0);

airsim.wait_key('Press any key to enable dust at 50%')
client.simSetWeatherParameter(airsim.WeatherParameter.Dust, 0.50);

airsim.wait_key('Press any key to enable fog at 50%')
client.simSetWeatherParameter(airsim.WeatherParameter.Fog, 0.50);

airsim.wait_key('Press any key to disable all weather effects')
client.simEnableWeather(False)