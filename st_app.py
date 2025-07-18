import streamlit as st

st.image('Logo.png', use_container_width=True)
st.title("👦🏻 User Profile Creator")
st.write("Fill in your information below:")

# Get user inputs
name = st.text_input("Full Name")
email = st.text_input("Email")
age = st.text_input("Age")

if st.button("Create Profile"):
    if not name or not email or not age:
        st.error("Please fill in all fields.")
    elif "@" not in email or "." not in email:
        st.error("Invalid email address.")
    elif not age.isdigit():
        st.error("Age must be a number.")
    else:
        # Clean and format data
        name = " ".join(word.capitalize() for word in name.strip().split())
        email = email.strip().lower()
        age = int(age)

        st.success("✅ Profile created successfully!")
        st.markdown("---")
        st.subheader("👦🏻 Your Profile")
        st.write(f"**Name:** {name}")
        st.write(f"**Email:** {email}")
        st.write(f"**Age:** {age}")

        # Age-based message
        if age < 18:
            st.info("🧒 You're a young learner. Keep it up!")
        elif age < 60:
            st.info("🧑‍💻 You're at a great stage to master Python!")
        else:
            st.info("🧓 It's never too late to learn something new!")
