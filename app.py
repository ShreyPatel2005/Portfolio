import streamlit as st
from PIL import Image
import base64
import os

# Page configuration
st.set_page_config(
    page_title="Shrey Patel",
    page_icon="assets/profile.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    /* Main content area */
    .main {
        margin-left: 220px;
        padding: 20px;
    }
    
    /* Vertical navbar */
    .sidebar .sidebar-content {
        width: 200px !important;
        background: white;
        border-right: 1px solid #e0e0e0;
        padding: 2rem 1rem;
        position: fixed;
        height: 100vh;
    }
    
    .nav-item {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 0.8rem 1rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        color: black;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.3s;
    }
    
    .nav-item:hover {
        background: #f5f5f5;
    }
    
    .nav-item.active {
        background: black;
        color: white;
    }
    
    /* Profile section */
    .profile-container {
        text-align: center;
        padding: 1rem 0 2rem;
        border-bottom: 1px solid #f0f0f0;
        margin-bottom: 1rem;
    }
    
    .profile-img {
        width: 180px;
        height: 180px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #f0f0f0;
        margin: 0 auto 1rem;
    }
    
    /* Tech stack icons */
    .tech-stack {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
        margin-top: 0.5rem;
        background: #1a1a1a;
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 0.5rem;
    }
    
    .tech-item {
        display: flex;
        align-items: center;
        gap: 8px;
        background: #FFFAFA;
        padding: 10px 15px;
        border-radius: 25px;
        color: black;
        
    }
    
    /* Skills carousel */
    .skills-carousel {
        display: flex;
        animation: scroll 20s linear infinite;
        gap: 40px;
        padding: 2rem 0;
    }
    
    @keyframes scroll {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
    }
    
    .carousel-container {
        overflow: hidden;
        position: relative;
        width: 100%;
    }
    
    .skill-logo {
        height: 60px;
        transition: transform 0.3s;
    }
    
    .skill-logo:hover {
        transform: scale(1.1);
    }
    
    /* Social icons */
    .social-icon {
        width: 42px;
        height: 42px;
        transition: transform 0.3s;
    }
    
    .social-icon:hover {
        transform: scale(1.1);
    }

</style>
""", unsafe_allow_html=True)

# Tech stack icons mapping (using icons8 logos)
tech_icons = {
    "Python": "https://img.icons8.com/color/84/python.png",
    "Pandas": "https://img.icons8.com/color/84/pandas.png",
    "NumPy": "https://img.icons8.com/color/84/numpy.png",
    "TensorFlow": "https://img.icons8.com/color/84/tensorflow.png",
    "PyTorch": "https://img.icons8.com/arcade/84/pytorch.png",
    "SQL": "https://img.icons8.com/color/84/sql.png",
    "Streamlit": "https://img.icons8.com/color/84/streamlit.png",
    "Flask": "https://img.icons8.com/color/84/flask.png",
    "MongoDB": "https://img.icons8.com/color/84/mongodb.png",
    "AWS": "https://img.icons8.com/color/84/amazon-web-services.png",
    "React": "https://img.icons8.com/color/84/react-native.png",
    "Docker": "https://img.icons8.com/color/84/docker.png",
    "Git": "https://img.icons8.com/color/84/git.png",
    "NodeJS": "https://img.icons8.com/color/84/nodejs.png"
}

# Navigation with icons
def navigation():
    with st.sidebar:
        profile_img_base64 = base64.b64encode(open("assets/profile.png", "rb").read()).decode() if os.path.exists("assets/profile.png") else ""
        st.markdown(f"""
        <div class="profile-container">
            <img src="data:image/png;base64,{profile_img_base64}" class="profile-img">
            <h2>Shrey Patel</h2>
            <p>Developer | Data Scientist</p>
            <div style="display: flex; gap: 15px; justify-content: center;">
                <a href="https://www.linkedin.com/in/shrey-patel-68597325b/" target="_blank">
                    <img src="https://img.icons8.com/color/64/linkedin.png" class="social-icon">
                </a>
                <a href="https://github.com/Shrey131005" target="_blank">
                    <img src="https://img.icons8.com/color/64/github.png" class="social-icon">
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Center wrapper for resume and learning section
        st.markdown("""
        <div style="text-align: center;">
        """, unsafe_allow_html=True)

        # Resume download button
        if os.path.exists("assets/resume.pdf"):
            with open("assets/resume.pdf", "rb") as pdf_file:
                resume_data = pdf_file.read()
            st.download_button(
                label="📄 Download Resume",
                data=resume_data,
                file_name="Shrey Patel_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )

        st.markdown("### 🚀 Currently Learning", unsafe_allow_html=True)
        st.markdown("""
        <ul style='list-style: none; padding-left: 0; text-align: left; display: inline-block;'>
            <li>🧠 Machine Learning</li>
            <li>🔐 OAuth 2.0</li>
            <li>📦 Docker </li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        

# Main content
def main():
    navigation()
    
    # Main content container
    with st.container():
        # Home Section
        st.markdown('<div id="home" class="section">', unsafe_allow_html=True)
        st.title("Hi, I'm Shrey Patel !")
        st.subheader("Full Stack Developer & Data Scientist")
        st.write("""
        I build intelligent systems that solve real-world problems through 
        data-driven approaches and elegant engineering solutions.
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **What I do:**
            - Machine Learning solutions
            - Data Analysis & Visualization
            - Web Application Development
            - Cloud Infrastructure
            """)
        
        with col2:
            st.markdown("""
            **Currently working on:**
            - AI-powered analytics platform
            - GIS Land Use Classification
            - Ecommerce Platform
            """)
        st.markdown('</div>', unsafe_allow_html=True)
        
                # Redesigned About Section Using Streamlit Features
        st.markdown('<div id="about" class="section">', unsafe_allow_html=True)
        st.header("About Me")

        with st.container():
            st.subheader("🎓 Education")
            st.info("""
            - **12th**  Gnyan Dham School (2023)
            - **10th**  Gnyan Dham School (2021)
            """)

        with st.container():
            st.subheader("💼 Experience")
            st.success("""
            - **Event Management** at IEEE SB PDEU (2025–Present)
            - **Tech Core** at SnT PDEU (2024–Present)
            """)

        # with st.container():
        #     st.subheader("🏆 Achievements")
        #     st.warning("""
        #     - Comming Soon...
        #     """)

        st.markdown('</div>', unsafe_allow_html=True)
        
        # Skills Section
        st.markdown('<div id="skills" class="section">', unsafe_allow_html=True)
        st.header("My Tech Stack")
        
        st.markdown("""
        <div class="carousel-container">
            <div class="skills-carousel">
                <img src="{python}" class="skill-logo">
                <img src="{pandas}" class="skill-logo">
                <img src="{numpy}" class="skill-logo">
                <img src="{tensorflow}" class="skill-logo">
                <img src="{pytorch}" class="skill-logo">
                <img src="{sql}" class="skill-logo">
                <img src="{aws}" class="skill-logo">
                <img src="{react}" class="skill-logo">
                <img src="{nodejs}" class="skill-logo">
                <img src="{docker}" class="skill-logo">
                <img src="{git}" class="skill-logo">
                <img src="{pandas}" class="skill-logo">
                <img src="{numpy}" class="skill-logo">
                <img src="{tensorflow}" class="skill-logo">
                <img src="{pytorch}" class="skill-logo">
                <img src="{sql}" class="skill-logo">
                <img src="{aws}" class="skill-logo">
                <img src="{react}" class="skill-logo">
                <img src="{docker}" class="skill-logo">
                <img src="{git}" class="skill-logo">
            </div>
        </div>
        """.format(
            python=tech_icons["Python"],
            pandas=tech_icons["Pandas"],
            numpy=tech_icons["NumPy"],
            tensorflow=tech_icons["TensorFlow"],
            pytorch=tech_icons["PyTorch"],
            sql=tech_icons["SQL"],
            aws=tech_icons["AWS"],
            react=tech_icons["React"],
            nodejs=tech_icons["NodeJS"],
            docker=tech_icons["Docker"],
            git=tech_icons["Git"]
        ), unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        st.divider()
        
        # Projects Section
        st.markdown('<div id="projects" class="section">', unsafe_allow_html=True)
        st.header("Featured Projects")
        st.header("")
        with st.container():
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image("assets/projects/project1.png", use_container_width=True)
            
            with col2:
                st.subheader("Shrivik Jewellery Ecommerce")
                st.write("""
                A fully Functional ecommerce platform for jewellery with user authentication, product management, and payment integration.
                """)
                
                st.markdown("""
                <div class="tech-stack" style="width: fit-content">
                    <span class="tech-item">
                        <img src="{react}" style="height: 20px;"> React
                    </span>
                    <span class="tech-item">
                        <img src="{mongodb}" style="height: 20px;"> MongoDB
                    </span>
                    <span class="tech-item">
                        <img src="{nodejs}" style="height: 20px;"> NodeJS
                    </span>
                </div>
                """.format(
                    react=tech_icons["React"],
                    mongodb=tech_icons["MongoDB"],
                    nodejs=tech_icons["NodeJS"],
                ), unsafe_allow_html=True)
                
                st.button("View Code", key="project1")
        
        st.divider()
        
        with st.container():
            col1, col2 = st.columns([2, 1])
            with col1:
                #add link to project
                st.markdown("<h3><a href='https://horizonlab.tech' target='_blank' style='text-decoration: none; color: inherit;'>HorizonLab.tech</a></h3>", unsafe_allow_html=True)

                st.write("""
                A Service Providing Platform for Web Development, App Development, and AI Solutions.
                """)
                
                st.markdown("""
                <div class="tech-stack" style="width: fit-content">
                    <span class="tech-item">
                        <img src="{react}" style="height: 20px;"> React
                    </span>
                    <span class="tech-item">
                        <img src="{mongodb}" style="height: 20px;"> MongoDB
                    </span>
                    <span class="tech-item">
                        <img src="{nodejs}" style="height: 20px;"> NodeJS
                    </span>
                </div>
                """.format(
                    react=tech_icons["React"],
                    mongodb=tech_icons["MongoDB"],
                    nodejs=tech_icons["NodeJS"],
                ), unsafe_allow_html=True)
                
                st.button("View Code", key="project2")
            
            with col2:
                st.image("assets/projects/project2.png", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.divider()

if __name__ == "__main__":
    main()
