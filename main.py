def on_forever():
    basic.pause(6900)
    for index in range(4):
        maqueen.servo_run(maqueen.Servos.S1, 70)
        basic.pause(200)
        maqueen.servo_run(maqueen.Servos.S1, 50)
        basic.pause(200)
    basic.pause(4000)
    for index2 in range(2):
        maqueen.servo_run(maqueen.Servos.S1, 150)
        basic.pause(200)
        maqueen.servo_run(maqueen.Servos.S1, 130)
        basic.pause(200)
    for index3 in range(3):
        maqueen.servo_run(maqueen.Servos.S1, 70)
        basic.pause(200)
        maqueen.servo_run(maqueen.Servos.S1, 50)
        basic.pause(200)
    for index4 in range(6):
        maqueen.servo_run(maqueen.Servos.S1, 150)
        basic.pause(200)
        maqueen.servo_run(maqueen.Servos.S1, 130)
        basic.pause(200)
    for index5 in range(4):
        maqueen.servo_run(maqueen.Servos.S1, 70)
        basic.pause(200)
        maqueen.servo_run(maqueen.Servos.S1, 50)
        basic.pause(200)
    maqueen.servo_run(maqueen.Servos.S1, 50)
    basic.pause(500)
basic.forever(on_forever)

def on_forever2():
    basic.pause(2500)
    for index6 in range(1):
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 40)
        basic.pause(200)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 40)
        basic.pause(200)
    maqueen.motor_stop(maqueen.Motors.ALL)
    basic.pause(200)
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 30)
    basic.pause(1000)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 30)
    basic.pause(200)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 25)
    basic.pause(100)
    maqueen.motor_stop(maqueen.Motors.ALL)
    basic.pause(2000)
    basic.pause(3000)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 90)
    basic.pause(400)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 90)
    basic.pause(400)
    maqueen.motor_stop(maqueen.Motors.ALL)
    for index7 in range(3):
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
        basic.pause(200)
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 50)
        basic.pause(200)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 25)
    basic.pause(200)
    maqueen.motor_stop(maqueen.Motors.ALL)
    basic.pause(1000)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 110)
    basic.pause(400)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 110)
    basic.pause(400)
    maqueen.motor_stop(maqueen.Motors.ALL)
    basic.pause(500)
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 30)
    basic.pause(500)
    maqueen.motor_stop(maqueen.Motors.ALL)
    basic.pause(1000)
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 30)
    basic.pause(500)
    maqueen.motor_stop(maqueen.Motors.ALL)
    basic.pause(1000)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 80)
    basic.pause(400)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 80)
    basic.pause(400)
    maqueen.motor_stop(maqueen.Motors.ALL)
    basic.pause(100)
    for index8 in range(2):
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 30)
        basic.pause(200)
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 30)
        basic.pause(200)
        maqueen.motor_stop(maqueen.Motors.ALL)
basic.forever(on_forever2)

def on_forever3():
    music.set_volume(120)
    music.set_tempo(180)
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(784, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(784, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(784, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(784, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(784, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(784, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(494, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(494, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(370, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.WHOLE))
basic.forever(on_forever3)

def on_forever4():
    basic.pause(6900)
    for index6 in range(4):
        maqueen.servo_run(maqueen.Servos.S2, 70)
        basic.pause(200)
        maqueen.servo_run(maqueen.Servos.S2, 50)
        basic.pause(200)
    basic.pause(4000)
    for index7 in range(2):
        maqueen.servo_run(maqueen.Servos.S2, 150)
        basic.pause(200)
        maqueen.servo_run(maqueen.Servos.S2, 130)
        basic.pause(200)
    for index8 in range(3):
        maqueen.servo_run(maqueen.Servos.S2, 150)
        basic.pause(200)
        maqueen.servo_run(maqueen.Servos.S2, 130)
        basic.pause(200)
    for index9 in range(6):
        maqueen.servo_run(maqueen.Servos.S2, 70)
        basic.pause(200)
        maqueen.servo_run(maqueen.Servos.S2, 50)
        basic.pause(200)
    for index10 in range(4):
        maqueen.servo_run(maqueen.Servos.S2, 70)
        basic.pause(200)
        maqueen.servo_run(maqueen.Servos.S2, 50)
        basic.pause(200)
    maqueen.servo_run(maqueen.Servos.S1, 50)
    basic.pause(500)
basic.forever(on_forever4)
