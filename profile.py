class customer:
      def __init__(self,name,email,phone_no,profile_image):
        self.name=name
        self.email=email
        self.phone_no=phone_no
        self.profile_image=profile_image
      def update_profile(self, name = None, email = None, phone_no = None, profile_image = None):
        if name:
            self.name=name
        if email:
            self.email=email
        if phone_no:
            self.phone_no=phone_no
        if profile_image:
            self.profil_image=profile_image
      def display_profile(self):
        print("Name:",self.name)
        print("email:",self.email)
        print("phone_no:",self.phone_no)
        print("profile_image:",self.profile_image)
customer1=customer("apoorva","apoorva@gmail.com","7676396192","profile_image.jpj")
customer1.display_profile()
customer1.display_profile()

        
        
        
        