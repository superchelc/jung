basic.forever(function () {
    basic.pause(6900)
    for (let index = 0; index < 4; index++) {
        maqueen.servoRun(maqueen.Servos.S2, 70)
        basic.pause(200)
        maqueen.servoRun(maqueen.Servos.S2, 50)
        basic.pause(200)
    }
    basic.pause(4000)
    for (let index = 0; index < 2; index++) {
        maqueen.servoRun(maqueen.Servos.S2, 150)
        basic.pause(200)
        maqueen.servoRun(maqueen.Servos.S2, 130)
        basic.pause(200)
    }
    for (let index = 0; index < 3; index++) {
        maqueen.servoRun(maqueen.Servos.S2, 150)
        basic.pause(200)
        maqueen.servoRun(maqueen.Servos.S2, 130)
        basic.pause(200)
    }
    for (let index = 0; index < 6; index++) {
        maqueen.servoRun(maqueen.Servos.S2, 70)
        basic.pause(200)
        maqueen.servoRun(maqueen.Servos.S2, 50)
        basic.pause(200)
    }
    for (let index = 0; index < 4; index++) {
        maqueen.servoRun(maqueen.Servos.S2, 70)
        basic.pause(200)
        maqueen.servoRun(maqueen.Servos.S2, 50)
        basic.pause(200)
    }
    maqueen.servoRun(maqueen.Servos.S1, 50)
    basic.pause(500)
})
basic.forever(function () {
    basic.pause(6900)
    for (let index = 0; index < 4; index++) {
        maqueen.servoRun(maqueen.Servos.S1, 70)
        basic.pause(200)
        maqueen.servoRun(maqueen.Servos.S1, 50)
        basic.pause(200)
    }
    basic.pause(4000)
    for (let index = 0; index < 2; index++) {
        maqueen.servoRun(maqueen.Servos.S1, 150)
        basic.pause(200)
        maqueen.servoRun(maqueen.Servos.S1, 130)
        basic.pause(200)
    }
    for (let index = 0; index < 3; index++) {
        maqueen.servoRun(maqueen.Servos.S1, 70)
        basic.pause(200)
        maqueen.servoRun(maqueen.Servos.S1, 50)
        basic.pause(200)
    }
    for (let index = 0; index < 6; index++) {
        maqueen.servoRun(maqueen.Servos.S1, 150)
        basic.pause(200)
        maqueen.servoRun(maqueen.Servos.S1, 130)
        basic.pause(200)
    }
    for (let index = 0; index < 4; index++) {
        maqueen.servoRun(maqueen.Servos.S1, 70)
        basic.pause(200)
        maqueen.servoRun(maqueen.Servos.S1, 50)
        basic.pause(200)
    }
    maqueen.servoRun(maqueen.Servos.S1, 50)
    basic.pause(500)
})
basic.forever(function () {
    basic.pause(300)
    for (let index = 0; index < 1; index++) {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CCW, 40)
        basic.pause(200)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 40)
        basic.pause(200)
    }
    maqueen.motorStop(maqueen.Motors.All)
    basic.pause(200)
    maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 60)
    basic.pause(1000)
    maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 30)
    basic.pause(200)
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 30)
    basic.pause(100)
    maqueen.motorStop(maqueen.Motors.All)
    basic.pause(2000)
    basic.pause(4800)
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 255)
    basic.pause(1200)
    maqueen.motorStop(maqueen.Motors.All)
    for (let index = 0; index < 3; index++) {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 50)
        basic.pause(200)
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CCW, 50)
        basic.pause(200)
    }
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 30)
    basic.pause(200)
    maqueen.motorStop(maqueen.Motors.All)
    basic.pause(1000)
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 255)
    basic.pause(1200)
    maqueen.motorStop(maqueen.Motors.All)
    basic.pause(3000)
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 255)
    basic.pause(1200)
    maqueen.motorStop(maqueen.Motors.All)
    basic.pause(100)
    for (let index = 0; index < 2; index++) {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 30)
        basic.pause(200)
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CCW, 30)
        basic.pause(200)
        maqueen.motorStop(maqueen.Motors.All)
    }
    basic.pause(5000)
})
basic.forever(function () {
    music.setVolume(120)
    music.setTempo(180)
    music.playTone(392, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Whole))
    music.playTone(784, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Whole))
    music.playTone(392, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Whole))
    music.playTone(784, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Whole))
    music.playTone(392, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(784, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(392, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(784, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(784, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(784, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(392, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(440, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(440, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(330, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(330, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(392, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(440, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(440, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(330, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(330, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(392, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(440, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(440, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(494, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(494, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(523, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(440, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(392, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(330, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(262, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Half))
    music.playTone(294, music.beat(BeatFraction.Quarter))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(294, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(330, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Quarter))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Quarter))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Quarter))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(294, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(330, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Quarter))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Quarter))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Quarter))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(294, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(330, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Quarter))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Quarter))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Quarter))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(370, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Whole))
})
