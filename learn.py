
class Participant:
    participantType = ""
    availableTime = 0
    name = ""

    def __init__(self, name):
      self.name = name
      self.stacks = []

    def addStacks(self,stack):
     self.stacks.extend(stack)

    def setMentorOrLearner(self, participantType):
      self.participantType = participantType

    def setAvailableTime(self, availableTime):
      if self.participantType == "mentor":
        self.availableTime = availableTime
    

class Learn:

   def __init__(self):
      self.participants = []

   def addParticipant(self, participant):
       self.participants.append(participant)

   def getMentor(self, stack, time):
       for participant in self.participants:
           if participant.participantType == "mentor":
               if stack in participant.stacks and participant.availableTime >= time:
                   print(participant.name)

p1 = Participant("M1")
p1.addStacks(["python", "java"])
p1.setMentorOrLearner("mentor")
p1.setAvailableTime(60)

p2 = Participant("L1")
p2.setMentorOrLearner("learner")

p3 = Participant("M2")
p3.addStacks(["python", "c#"])
p3.setMentorOrLearner("mentor")
p3.setAvailableTime(60)

p4 = Participant("M3")
p4.addStacks(["c"])
p4.setMentorOrLearner("mentor")
p4.setAvailableTime(70)

l = Learn()
l.addParticipant(p1)
l.addParticipant(p2)
l.addParticipant(p3)
l.addParticipant(p4)



print("Available Mentors are : ")
l.getMentor("python",30)


