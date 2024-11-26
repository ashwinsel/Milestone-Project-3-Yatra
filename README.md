# Yaatra - Spiritual Tours Guide
###### Code Institute / Backend for a web application using Python and a micro-framework / Milestone Project 3
[View Live Project Here][def42]

As a part of Milestone Project 3, this project demonstrates the use of non-relational databases with Flask and Python. The website serves as a platform where visitors can create and manage reviews about spiritual sites in India. It aims to foster a community of spiritual travelers, providing valuable insights and recommendations for future visitors.

### Purpose and Target Audience
The primary purpose of this platform is to connect spiritual travelers, tour operators, and cultural enthusiasts, offering a space to share and discover detailed reviews of spiritual journeys. By focusing on the unique aspects of spiritual and religious travel, the platform aims to stand out from other travel review websites.

![Screenshot][def24]

---

## **Index - Table of Contents**
------------

+ [User Experience (UX)](#-user-experience-ux)
    * [User Stories](#user-stories)             
+ [UX Planes](#ux-planes)
    * [Strategy](#strategy)
        - [Project Goals](#project-goals) 
        - [Customer Goals](#customer-goals)
        - [Company Goals](#company-goals)
        - [Future Implementations][def3]
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)     
    * [Surface](#surface)
        - [Colour Scheme](#colour-scheme)
        - [Typography](#typography)
        - [Imagery](#imagery)
+ [Features](#features)
    * [Home Page](#home-page)
    * [Browse Site Page](#browse-site-page)
    * [Read Insights Page](#read-insights-page)
    * [Edit Sites page](#edit-sites-page)
    * [Edit Insights page](#edit-insights-page)
    * [Register Page](#register-page)           
+ [Traceability Matrix](#traceability-matrix)
+ [Logic](#logic)
+ [Database Structure](#database-structure)
+ [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
+ [Testing](#testing)
    * [Validator Testing Results](#validator-testing-results)
        
    * [Lighthouse Testing](#lighthouse-testing)
        
+ [Responsiveness Testing Results](#responsiveness-testing-results)
+ [Bugs and Fixes](#bugs-and-fixes)
+ [Browser Compatibility](#browser-compatibility)
+ [Deployment and Cloning](#deployment-and-cloning)
+ [Credits](#credits)
    * [Content](#content)
    * [Code](#code)
    * [Media](#media)
+ [Gratitude](#gratitude)

---

## **User Experience (UX)**

### **User Stories**

| **App Function**                    | **As a/an**                     | **I want to be able to...**                                 | **So that I can...**                                        |
|-------------------------------------|----------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| **1. Viewing and Navigation**       | Visitor                         | Browse spiritual sites and journey insights                 | Explore potential destinations and learn from others' experiences |
|                                      | Visitor                         | View detailed information about a site                      | Understand the significance and plan my visit               |
|                                      | Visitor                         | Filter spiritual sites by region                   | Narrow down my search based on my specific interests        |
|                                      | Visitor                         | Search for a specific site or insight                       | Quickly find information about a particular location or experience |
|                                      | Visitor                         | Access the website on mobile or desktop devices             | Have a seamless browsing experience across devices          |
|                                      | Visitor                         | Navigate easily between pages       | Find the content I’m looking for without confusion          |
| **2. Registration and User Accounts** | Visitor                         | Register for an account                                      | Access features like adding, editing, or deleting entries   |
|                                      | Registered User                 | Log in to my account                                         | Manage my spiritual site entries and journey insights       |
|                                      | Registered User                 | Log out of my account                                        | Ensure my account information remains secure                |
| **3. Sites Management**              | Registered User                 | Add new spiritual sites                                      | Contribute to the database and help the community grow      |
|                                      | Registered User                 | Edit existing sites I created                               | Update or correct details for accuracy                      |
|                                      | Registered User                 | Delete sites I created                                       | Remove outdated or incorrect entries                        |
|                                      | Visitor                           | View all site submissions                                   | Learn about various sites and plan my travel             |
| **4. Insights Management**          | Registered User                 | Add a journey insight                                       | Share my travel experience and help others                  |
|                                      | Registered User                 | Edit insights I created                                     | Update or correct details of my reviews                     |
|                                      | Registered User                 | Delete insights I created                                   | Remove content that is no longer relevant                   |
|                                      | Visitor                         | View insights shared by others                              | Learn from the experiences of fellow travelers              |
| **5. Searching and Filtering**      | Visitor                         | Filter sites dynamically based on region and deity          | Easily find relevant sites that match my criteria           |
|                                      | Visitor                         | Search for a site by typing a keyword (e.g., deity name)    | Easily find relevant sites that match my criteria      |
| **6. Usability Enhancements**       | Visitor                         | View prominent links to "Browse Sites" and "Read Insights"  | Quickly access the main features of the site from the homepage |
|                                      | Visitor                         | Understand filtering instructions with clear prompts        | Avoid confusion when using input fields        |
| **7. Validation and Security**      | Registered User                 | Receive validation messages when filling forms              | Ensure I’m entering valid and complete information          |
| **8. Visual Design and Accessibility** | Visitor                         | Experience a visually appealing and accessible design       | Have an enjoyable and inclusive browsing experience         |
|                                      | Visitor                         | Use a consistent color scheme and typography               | Focus on content without distractions                       |

---

## **UX Planes**
------------
- ### **Strategy**
    * Make it easier for users planning a tour to spiritual destinations around India. Provide a platform for sharing reviews of tour operators and spiritual sites in India. Facilitate community engagement and knowledge sharing.
    + #### Project Goals
    * This includes User Authentication: Registration, login, profile management. Review Management: Create, edit, update and delete journey insights. Site Information: Create, edit, update and delete spiritual sites, browse existing sites. Filter spiritual sites based on certain attributes.
    * Being able to access all devices.
    + #### Customer Goals
    * The focus is on meeting the needs of users, both first-time visitors and returning users. 
    * Visitors: Access reviews, browse spiritual sites, and plan travel routes.
    * Registered Users:** Create and manage profiles, submit and edit reviews, suggest new sites and routes.
    + #### Future Implementations
    * Additional Social Media Integrations: Integrating other platforms like Facebook and Twitter for broader user engagement. Expanded Database: Continuously updating the database with more spiritual sites and user-generated content. Advanced Features: Implementing features like user forums, travel itineraries, and recommendation algorithms to enhance user experience.
- ### **Scope**
    - The scope of the Yaatra website encompasses creating a user-friendly and accessible web interface that allows users to:
        * Users can create and manage their profiles. Only the profile owner can edit or delete their reviews, ensuring authenticity and control.
        * Users can write detailed reviews about their experiences with tour operators, routes taken, and spiritual sites visited.
        * Users can contribute information about new spiritual sites that are not yet listed on the platform, enriching the database.
        * Users can browse through an extensive list of potential spiritual sites to visit.
        * Users can add and suggest possible routes that connect specific religious sites, helping others plan their journeys.
- ### **Structure**
    - The Structure Plane outlines how the information and functionalities are organized.
        * Home Page: Introduction, Navigation to other parts, Option to Register or just Browse.
        * Sites Section: List of sites, add new site, update or delete a site.
        * Insights Page: Create review, browse reviews, review details.
        * Navigation: Top navigation bar with links to Home, Reviews, Sites, Routes, Profile, and Admin (if applicable).
        * Forms: Registration, login, review submission, site and route suggestion forms.
        * Search and Filter: Search bar and filters for reviews, sites, and routes.
- ### **Skeleton**
    + #### Wireframes
        ![Home Page Wireframe][def4]
        ![Events Page Wireframe][def5]                    
- ### **Surface**
    + #### Colour Scheme
        * I have used a rusted copper ztar color palette consistent with the backgorund image of a ethereal map image.
        * #CD8D47 a shade of dark green, black, and a dark rusty font colors play a good contrast to the chosen colour palette.

        ![Colour Scheme][def29]        

    + #### Typography
        ### Typography Used in the CSS

1. **Fonts Imported:**
   - **'Lord Spirit':** Imported from `https://fonts.cdnfonts.com/css/lord-spirit`.
   - **'Lumanosimo':** Imported from `https://fonts.cdnfonts.com/css/lumanosimo`.

2. **Font Families Applied:**
   - **'Lumanosimo', sans-serif:** Applied globally to the entire body, ensuring that the text throughout the website is primarily set in this font.
   - **'Lord Spirit', sans-serif:** Specifically used for the `.brand-logo` in the navigation bar to give it a distinctive and visually striking appearance.

### Detailed Write-Up

#### 1. **'Lumanosimo' Font:**
   - **Usage:** 
     - This font is the primary typeface for the website and is applied globally across most of the text elements, such as the body text and `.banner-text`. It ensures consistency and coherence in the visual language of the site.
   - **Styling:**
     - The font is paired with a sans-serif fallback to maintain legibility in cases where the custom font fails to load.
     - Additionally, text shadows are applied to the body text using `text-shadow: 2px 2px 2px rgba(234, 194, 134, 0.5);`. This effect adds depth and a subtle glow to the text, enhancing its readability against varied backgrounds.

#### 2. **'Lord Spirit' Font:**
   - **Usage:** 
     - This font is exclusively used for the `.brand-logo` in the navigation bar. The large size (`font-size: 3em;`) and unique styling of 'Lord Spirit' create a distinct identity for the brand name, making it stand out on the page.
   - **Styling:**
     - The font is paired with a sans-serif fallback to maintain consistency in appearance and ensure that the brand logo remains visually appealing, even if the custom font is not available.
     - The font color is set to `#031929`, a dark blue that contrasts well with the background, ensuring that the logo is easily recognizable.

### Typography Implementation

The chosen typography reflects the spiritual and elegant nature of the "Yaatra Spiritual Tours Guide" website. 

- **'Lumanosimo'** provides a balance between readability and a touch of sophistication, suitable for the descriptive and narrative content of the website. The text-shadow effect enhances the spiritual and ethereal feel, which aligns with the theme of spiritual tours.
  
- **'Lord Spirit'** contributes to brand recognition by making the logo striking and memorable. Its decorative style is likely intended to evoke a sense of tradition and cultural richness, which resonates with the spiritual focus of the site.

* Responsive Design Considerations

- The font sizes are adjusted in the media queries to ensure readability across different screen sizes. For instance, the brand logo's font size decreases on smaller screens (`2em` for tablets and `1.5em` for mobile devices), maintaining visual hierarchy without overwhelming the smaller display areas.
- Similarly, the `.banner-text` and button text sizes are reduced on smaller screens to ensure the layout remains clean and accessible, avoiding text overflow and maintaining a harmonious design.
    + #### Imagery
        ![backgroundimage][def46]
        *   This image is ideal for use in the banner or hero section of your website, especially on the homepage. The vibrant and captivating visual of iconic Indian landmarks symbolizes spirituality, culture, and the essence of India's spiritual heritage, perfectly aligning with the theme of "Yaatra Spiritual Tours Guide."
        * ![favicon][def49] The favicon was designed using an online favicon generator. This has been designed with an image that has a man sat inbetween coloured aura and chakra through. This makes it to able to spot amongst several tabs in the browser.
        * All the images used are license free or been used with owners consent. The sources are listed in the Credits section.
        * Images used were compressed using Tinypng.com for better performance and user experience.

## **Features**
------------
- ### Home page
#### 1. **Header Section with Slider**
   - **Hero Slider (`.hslider`):**
     - The homepage opens with a dynamic slider, featuring two distinct slides that introduce users to the core offerings of "Yaatra" – a guide for spiritual travelers.
     - **Slide 1:** 
       - *Title*: "Yaatra" - The site title is displayed in an elegant and grand font, 'Lord Spirit,' emphasizing the spiritual essence of the platform. The large font size (6rem) ensures the title is the focal point, grabbing the user's attention immediately.
       - *Tagline*: "Guide for Spiritual Travellers" - This succinct tagline conveys the purpose of the platform, helping visitors understand what the website is about at a glance.
       - *Call to Action*: 
         - If the user is not logged in, they see options to either "Sign In" or "Register," each button styled with a teal darken-1 background, ensuring they stand out against the banner's background. Icons like the sign-in and user-plus symbols enhance usability and visual appeal.
     - **Slide 2:**
       - *Title*: "Just want to Browse?" - This slide addresses users who may not want to sign up immediately, offering an inviting alternative to explore the site.
       - *Tagline*: "No Problem!" - Reinforces the inclusive approach of the platform, making all users feel welcome.
       - *Call to Action*: Buttons are provided to "Browse Sites" and "Read Journey Insights," ensuring easy navigation to key sections of the website. Each button is clearly labeled with an accompanying icon (e.g., book and read icons), making it visually intuitive.

#### 2. **Main Content Section (`.container`)**
   - **Information Cards (`.card-panel`):**
     - This section uses a three-column grid layout to present key features in a visually balanced and accessible manner. Each column contains a card with a header and a brief description, making the information digestible and easy to scan.

   - **Feature 1: About Us**
     - *Description*: 
       - The "About Us" card introduces the platform, highlighting its role in connecting a community of spiritual travelers. It emphasizes the platform's user-driven nature, where insights and information are shared to aid in planning spiritual journeys.
       - *Context*: 
         - The text mentions the surge in spiritual travel searches in India, framing the platform as a timely and relevant resource for modern spiritual travelers.
- ### Browse Site page
### Detailed Features on the "Browse Sites" Page

#### 1. **Header Section**
   - **Interactive Filter Options:**
     - The "Browse Sites" page begins with a highly interactive filtering system designed to help users easily navigate through the numerous spiritual sites available on the platform.
     - **Filtering by Part of India:**
       - Users can filter the sites based on different geographical regions of India. The filter dropdown allows the selection of specific parts, making it easier for users to explore sites relevant to their travel plans.
     - **Filtering by Deity:**
       - Another dropdown filter lets users narrow down the sites by the deity associated with them. This feature is particularly useful for those looking to visit temples or locations dedicated to a particular deity.
     - **Filter Button:**
       - Once the filters are set, users can apply them using the "Filter" button, which is prominently styled with a black-text-on-orange background, ensuring it's noticeable and easy to use.

   - **Add Site Option (Visible to Logged-In Users Only):**
     - Logged-in users are presented with an option to "Add Site," empowering the community to contribute by adding new spiritual sites to the directory. The button is styled with an orange lighten-2 background, making it visually distinct. It includes an icon (fa-plus) to emphasize its purpose clearly.
     - This feature fosters a collaborative environment, encouraging user-generated content that can benefit others in the community.

   - **Instructional Text:**
     - A small, clear instruction is provided at the top, advising users on how to activate the dropdown filters. This ensures a smooth user experience, particularly for those unfamiliar with the interface.

#### 2. **Body Section**
   - **Collapsible List of Spiritual Sites:**
     - The main body of the page features a collapsible list that dynamically displays the spiritual sites based on the applied filters. The collapsible structure is user-friendly, allowing for a clean and organized presentation of information.
     - **Collapsible Headers:**
       - Each site is introduced with a collapsible header that includes:
         - *Site Name*: Displayed in bold, ensuring that the name of each site stands out.
         - *Icon*: A gopuram icon (fa-gopuram) is used to symbolize temples and spiritual sites, adding a culturally relevant visual cue.
         - *Accessibility Indicator*: If a site is wheelchair accessible, a wheelchair icon is displayed alongside the site name, providing crucial information for users with mobility needs.
       - **Edit and Delete Options (Conditional Display):**
         - If the logged-in user is the creator of a particular site, additional buttons for editing and deleting the site appear within the header. These buttons are styled distinctly (yellow for edit, red for delete) to differentiate their functions, with text-shadow effects to enhance visibility against different backgrounds.
   
   - **Collapsible Body:**
     - When a user clicks on a site's header, the collapsible body expands to reveal detailed information about the site:
       - *Deity*: The specific deity associated with the site is clearly mentioned, aiding users in understanding the religious significance of the location.
       - *Part of India*: This detail situates the site geographically, helping users in their travel planning.
       - *Description*: A comprehensive description of the site is provided, offering users insight into its historical, cultural, and spiritual importance.
- ### Read Insights page
### Detailed Features on the "Read Insights" Page

#### 1. **Header Section**
   - **Page Title:**
     - The "Read Insights" page opens with a clear and centered title, "Journey Insights," setting the stage for users to delve into personal stories, reviews, and insights shared by other spiritual travelers. The title's positioning at the center enhances its visibility and immediately informs users about the page's content.
   
   - **Add Insight Button (Conditional Display):**
     - For logged-in users, the page offers an "Add Insight" button prominently displayed beneath the title. 
     - **Button Styling and Iconography:**
       - The button is styled with an orange lighten-2 background and black text, maintaining a consistent design with other interactive elements across the site. The inclusion of a "fa-plus" icon makes the button's purpose clear at a glance—inviting users to contribute their own travel experiences to the platform.
     - **User Empowerment:**
       - This feature not only encourages user-generated content but also empowers the community to share valuable information and personal experiences, enriching the collective knowledge available on the platform.

#### 2. **Body Section**
   - **Grid Display of Insights:**
     - The main body of the page is designed as a grid layout, effectively organizing multiple user insights into a visually appealing and easily navigable structure. This layout allows for the simultaneous display of numerous insights without overwhelming the user, facilitating easy browsing and comparison of different experiences.
     - **Grid Item Composition:**
       - Each grid item represents an individual user insight and is thoughtfully composed to highlight key aspects of the travel experience:
         - **Location Name:** The name of the location is prominently displayed as the heading of each grid item, immediately informing users about the specific spiritual site or journey being discussed.
         - **Visit Date:** The exact date of the visit is formatted as "dd.mm.yyyy," providing a clear reference to when the experience took place. This is crucial for contextualizing the insight, as experiences may vary depending on the time of year or recent developments at the site.
         - **Rating:** Users can see how the experience was rated, offering a quick indication of the overall satisfaction with the journey.
         - **Purpose of Visit:** This field explains the intent behind the visit, such as pilgrimage, meditation, or cultural exploration, helping others with similar motivations to gauge the relevance of the insight.
         - **Review Description:** A detailed review is provided, where users share their personal experiences, thoughts, and any advice they may have for future visitors. This rich content forms the core value of the page, offering authentic, firsthand accounts of spiritual journeys.
         - **Created By:** The review's author is credited at the bottom of each grid item, fostering a sense of community and accountability. Knowing the author can also help users reach out or connect with others who have similar interests.

   - **Edit and Delete Options (Conditional Display):**
     - If the logged-in user is the creator of a particular review, they are given additional options to edit or delete their insight:
       - **Edit Button:** Allows users to make changes to their original insight, ensuring that information remains accurate and up-to-date. The button is styled in yellow accent-3 with black text, making it distinct but complementary to the overall design.
       - **Delete Button:** Users can also choose to delete their insight if it is no longer relevant or if they wish to remove it for any other reason. The delete button is styled with a red darken-4 background and black text, with a subtle text-shadow effect for emphasis. This styling alerts users to the button's significance, reducing accidental deletions.
     - **Conditional Logic:** The edit and delete buttons are only visible to the author of the insight, ensuring that users have control over their contributions while preventing unauthorized changes.
- ### Edit Sites page
### Detailed Features on the "Edit Site" Page

#### 1. **Header Section**
   - **Page Banner:**
     - The header section opens with a banner that communicates the page’s purpose: allowing users to update and refine existing site entries.
     - **Message Content:**
       - The banner text, “Want to Edit a Site Entry? We're always want to keep our community's knowledge and experiences up-to-date,” is designed to encourage users to contribute to the platform's accuracy and relevance. It highlights the importance of maintaining up-to-date information, fostering a collaborative spirit.
     - **Text Styling:**
       - The text is centrally aligned, with the primary call to action ("Want to Edit a Site Entry?") underlined for emphasis, drawing attention to the page's functionality.

#### 2. **Body Section**
   - **Form Structure:**
     - The main body contains a well-organized form that allows users to update information about a specific spiritual site. The form is centrally placed and neatly presented within a card panel, ensuring a clean, user-friendly experience.

   - **Input Fields:**
     - **Site Name Input Field:**
       - **Icon and Field:** The site name is prefixed by a "fa-gopuram" icon, visually associating the field with the cultural or spiritual significance of the site. The field enforces a text pattern validation and limits input to between 2 and 100 characters, ensuring that names are correctly formatted and of appropriate length.
       - **Pre-filled Value:** The input field is pre-filled with the existing site name, making it easy for users to identify and edit as needed.
       - **Label Styling:** The label for the site name is styled in black text, maintaining a consistent theme, and is set as active to indicate that the field is pre-populated.

     - **Deity Field:**
       - **Icon and Field:** The deity associated with the site is represented by a "fa-hands-praying" icon. The input field requires text input with a pattern allowing between 2 and 20 characters, reflecting the deity's name. This field is marked as required, emphasizing its importance in describing the site.
       - **Validation:** The validation ensures that users input a proper name, avoiding any formatting errors.
       - **Pre-filled Value:** The field is pre-filled with the current deity name, simplifying the editing process.

     - **Part of India Location Selection:**
       - **Icon and Dropdown:** The dropdown is prefixed with a "fa-compass" icon, symbolizing direction or location. Users can select the part of India where the site is located from a predefined list.
       - **Dynamic Selection:** The dropdown automatically highlights the part of India currently associated with the site, thanks to the conditional selection logic, making the editing process straightforward.
       - **Label:** The label is actively displayed, and the field is required to ensure this essential information is captured.

     - **Description Field:**
       - **Icon and Textarea:** The description field, preceded by a "fa-rectangle-list" icon, allows users to provide detailed information about the site. The textarea enforces a character count between 5 and 800, giving enough room for detailed descriptions while preventing overly lengthy entries.
       - **Pre-filled Text:** The textarea is pre-filled with the site's existing description, making it easy for users to revise or update the content.
       - **Label:** The label remains active and styled in black text, ensuring clarity in what the field is asking for.

     - **Disabled Access Checkbox:**
       - **Checkbox and Icon:** The disabled access feature is represented by a checkbox with an adjacent "fa-wheelchair" icon, making the feature easily recognizable. The checkbox is pre-checked if the site currently has disabled access, reflecting the existing data.
       - **Label and Tooltip:** The label encourages inclusivity by highlighting the importance of noting whether the site is accessible to those with disabilities.

   - **Submit Button:**
     - **Button Placement and Styling:**
       - The submit button is centrally placed within the form, with the text "Update" indicating the action's purpose. The button is styled with an orange background and black text, consistent with the site's design palette, ensuring it stands out as the primary call to action on the page.
       - **Iconography:** Although no additional icon is present with the button text, the straightforward design and color contrast make the button highly visible and inviting.
- ### Edit Insights page
### Detailed Features on the "Edit Insights" Page

#### 1. **Header Section**
   - **Page Banner:**
     - The header section features a prominent banner that outlines the purpose of the page: enabling users to edit their previously shared journey insights.
     - **Message Content:**
       - The banner text reads, “Want to Edit a Journey Insight? We're always want to keep our community's knowledge and experiences up-to-date,” which serves as a prompt for users to refine and update their insights, reinforcing the collaborative nature of the platform.
     - **Text Styling:**
       - The primary call to action, “Want to Edit a Journey Insight?” is underlined for emphasis, ensuring it grabs the user’s attention. The text is center-aligned, making it easily readable and visually appealing.

#### 2. **Body Section**
   - **Form Structure:**
     - The main body contains a structured form that allows users to update their journey insights. This form is centrally located within a card panel, providing a clean and organized layout that is easy to navigate.

   - **Input Fields:**
     - **Where Did You Go Field:**
       - **Icon and Field:** This field is designed to capture the name of the location visited, prefixed with a "fa-gopuram" icon to symbolically represent the nature of the journey. The field accepts text input with a validation pattern, requiring the input to be between 2 and 100 characters, ensuring the entry is concise yet descriptive.
       - **Pre-filled Value:** The field is pre-filled with the existing location name, making it simple for users to make adjustments if necessary.
       - **Label Styling:** The label for this field is set to active with black text, maintaining consistency with the page's overall design.

     - **Rating Field:**
       - **Icon and Field:** This field is dedicated to capturing the user’s rating of their experience, represented by a "fa-hands-praying" icon. The field requires text input, ensuring that the rating is formatted correctly within a 2 to 20 character limit.
       - **Pre-filled Value:** The field is pre-filled with the current rating, allowing users to easily update their experience rating.
       - **Label Styling:** The label is active, providing clarity on what information the field is requesting.

     - **When Did You Go Field:**
       - **Icon and Datepicker:** The visit date field is marked with a "fa-calendar-alt" icon, linking it to the idea of time or scheduling. It includes a date picker for ease of use, allowing users to select the date they visited the site. This date is formatted as "dd.mm.yyyy" and is pre-filled based on the existing data.
       - **Label:** The label is actively displayed above the date picker, ensuring users understand the field's purpose.

     - **Purpose Field:**
       - **Icon and Field:** The purpose of the visit is captured in this field, marked with a "fa-rectangle-list" icon, symbolizing a list or explanation. This text input requires the purpose to be concise, falling between 2 and 20 characters.
       - **Pre-filled Value:** The field comes pre-filled with the user's previously stated purpose, streamlining the editing process.
       - **Label:** The label remains active, clearly communicating the field’s intent.

     - **Description Field:**
       - **Textarea and Label:** This textarea is where users can elaborate on their experience. The field is styled to be center-aligned with a clear, prominent label reading, “Tell Us More About Your Experience!” This encourages detailed and thoughtful input, with the field requiring between 5 and 800 characters.
       - **Pre-filled Text:** The textarea is pre-filled with the existing review description, allowing for easy updates and revisions.
       - **Label Styling:** The label is styled in black text to remain consistent with the other fields, ensuring the page maintains a cohesive look.

   - **Submit Button:**
     - **Button Placement and Styling:**
       - The submit button is prominently placed at the bottom of the form, with the text "Update" clearly indicating its function. The button is styled with an orange background and black text, matching the site’s design scheme. This ensures the button stands out as the primary call to action on the page.
       - **Iconography:** The button does not include an additional icon, but the color contrast and central placement make it immediately noticeable and easy to interact with.
- ### Register page
### Detailed Features on the "Register" Page

The "Register" page is designed to provide a seamless and user-friendly experience for new users to create an account on the platform. Below is a breakdown of the key features and elements of the page:

#### 1. **Header Section**
   - **Page Banner:**
     - The banner at the top of the page serves as a prompt for users who might already have an account.
     - **Text Content:**
       - The banner text reads, “Already Have a Profile?” followed by a link, “Sign In Here!” which directs users to the login page if they are existing members.
     - **Link Styling:**
       - The "Sign In Here!" link is styled with a light-blue text color (`text-darken-4`), making it stand out against the rest of the banner text. This provides a clear call-to-action for existing users while maintaining the page's overall aesthetic.

#### 2. **Body Section**
   - **Form Layout:**
     - The registration form is centrally located within a card panel, ensuring that it is the focal point of the page. The form uses a simple and clean layout that guides the user through the registration process step-by-step.

   - **Input Fields:**
     - **Username Field:**
       - **Icon and Field:** The username field is accompanied by a "fa-user-plus" icon, which visually represents user creation. The input field is set up to accept an alphanumeric username between 5 and 8 characters in length.
       - **Validation and Requirements:** The input field has validation rules enforcing the character length and type, ensuring that the username meets the platform’s criteria.
       - **Label and Helper Text:** The label, “Username,” is styled in black text and is accompanied by helper text that clearly explains the required format: “An alphanumeric value of 5-8 characters.”

     - **Password Field:**
       - **Icon and Field:** The password field is identified with a "fa-lock" icon, indicating security. Users are required to create a password with similar constraints to the username: an alphanumeric string between 5 and 8 characters.
       - **Validation:** The password field includes validation to ensure that the input meets the required format.
       - **Label and Helper Text:** The label, “Password,” is also in black text, with helper text explaining the requirements, “An alphanumeric value of 5-8 characters.”

     - **Confirm Password Field:**
       - **Icon and Field:** This field is similar in appearance to the password field, also using the "fa-lock" icon, but its purpose is to confirm the user's password. It ensures that users correctly enter their intended password by requiring them to input it twice.
       - **Validation:** The field includes validation to check that the confirm password matches the initial password input, reducing errors during registration.
       - **Label and Helper Text:** The label is clear, and the helper text reminds users to “Ensure this matches the password above.”

   - **Register Button:**
     - **Button Styling and Placement:**
       - The "Register" button is styled prominently with a large, full-width design in black with white text. This ensures it is the most noticeable element on the page and is placed at the bottom of the form to conclude the registration process.
       - **Iconography:** The button includes a "fa-sign-in-alt" icon, reinforcing the idea of signing up or registering for the platform.
       - **Action:** Clicking the button submits the form data for processing, initiating the registration of a new user account.
------------            
- ### Traceability Matrix
    ![Table][def74]
------------
- ## **Logic**
    * The initial flowchart designed to base the app routes is as follows:
    ![Flowchart][def25]
------------ 
- ## **Database Structure**
    * Database Structure and Collections
Collections:
locations: Stores information about various sites. The documents in this collection include fields like site_name, deity, part_name, description, access, and created_by.
user: Contains user credentials for authentication. Documents in this collection have fields such as username and password.
part: Likely used to store distinct part names for dropdowns in forms. It includes at least the field part_name.
reviews: Stores user-generated reviews for sites. Documents include fields such as where, rating, visit_date, purpose, review_des, and created_by.
Database Operations
User Authentication and Management:

Registration: Users can register with a unique username and password. Passwords are hashed before being stored.
Login: Users can log in using their username and password. Passwords are verified against stored hashes.
Logout: Logs out the current user by removing the username from the session.
Site Management:

Adding Sites: New sites can be added to the locations collection with details like site_name, deity, part_name, description, and access. The site is also tagged with the username of the creator.
Editing Sites: Existing site information can be updated. The document in the locations collection is modified based on its _id.
Deleting Sites: Sites can be removed from the locations collection based on their _id.
Insights/Reviews Management:

Adding Reviews: Users can submit reviews, which are stored in the reviews collection. Reviews include fields for the review's location, rating, visit date, purpose, and description.
Editing Reviews: Reviews can be edited by updating the corresponding document in the reviews collection.
Deleting Reviews: Reviews can be deleted based on their _id.
Filtering and Browsing:

Filter Sites: Allows users to filter sites based on part_name and deity.
Browse Sites: Displays all sites or those filtered by user criteria.
------------    
- ## **Technologies Used**
------------
+ ### Languages Used
    * #### HTML5
    * #### CSS3
    * #### Javascript (Jquery)
    * #### Python
+ ### Frameworks, Libraries and Programs Used
    * #### [Cdnfonts][Cdnfonts] : was used to import Samarkan fonts into style.css file which has been used in the Main Logo title.
    * #### [Font Awesome][def9] : was used to add icons for aesthetic and UX purposes.
    * #### [Git][def10]: was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
    * #### [GitHub][def11] : It is used as the repository for the project's code after being pushed from Git.
    * #### [Balsamiq][def13] : was used to create the wireframes during the design process.
    * #### [Coolors][def14] : was used to find complimenting colors to the backgorund image for the website color palette.
    * #### [Materialize][def17] : codes from Materilaize has been used to create various aspects, especially, call out buttons, card panels, slider etc..
    * #### [Autoprefixer CSS online][def18] : has been used to parse the CSS in style.css to add different browser prefixes to ensure the CSS works on all browsers.
    * #### [favicon.io][def19] : was used to generate the favicon for the website.
    * #### [W3C Markup Validation Service][def20] : has been used to validate the code on all pages and style.css.
    * #### [UI.Dev][def22] : was used to generate Mockup Screenshots.
    * #### [Free Formatter][def23] : was used to ensure proper indentation in the HTML and CSS codes.
    * #### MOngoDB has been used to create database
    
- ## **Testing**
------------
+ ### Validator Testing Results
    * Javascript was tested using JSHint
    JSHint highlighted some undefined variables and unused functions. These were due to them being used/accessed from within the HTML pages rather than within the script itself.

    * Css was validated using https://jigsaw.w3.org/css-validator/#validate_by_input+with_options
    No issues found

    * My code did not pass the Code Institute Linter for Python.
    I was unable to fix some errors such as line length as it was interfering with my code. I will read up more regarding Pep8 compliance and how to code accordingly. In future projects I intend to validate as i go along. Or perhaps even install one of the formatter packages.
    
+ ### Lighthouse Testing
Results
![HomePage][def50]
![BrowseSites][def64]
![ReadInsight][def65]
![Register][def66]
![SignIn][def67]
![AddInsight][def68]
![AddSite][def47]

    

+ ### Responsiveness Testing Results
    ![Results][def26]
    ![Results][def27]
    ![Results][def28]
    ![Results][def30]
    ![Results][def31]
    ![Results][def32]
    ![Results][def45]

---

## **Bugs and Fixes**

**1. Issue with Dynamic Dropdown Behavior in "Select Part of India"**
Bug Encountered: The dropdown for "Select Part of India" required users to manually click "Apply Filters" once to load options dynamically. This behavior was unintuitive, and users often did not understand why the dropdown was empty.

Root Cause: The dropdown relied on backend data fetched asynchronously but lacked an automated trigger or preloading mechanism.

Resolution: A dedicated /get_part_names route was created to fetch the dropdown data dynamically. JavaScript AJAX was used to trigger this call on page load, ensuring the dropdown was populated seamlessly without user intervention.

**2. Continuous Triggering of Filters on Page Load**
Bug Encountered: Auto-triggering the "Apply Filters" button caused continuous loops of the action, leading to poor performance and usability.

Root Cause: The JavaScript lacked proper state management, resulting in infinite event triggering.

Resolution: A triggered flag was introduced to ensure the button auto-triggered only once. This resolved the infinite loop issue and ensured the button remained functional for manual usage.

**3. Case Sensitivity and Limited Flexibility in Deity Filtering**
Bug Encountered: The "Select Deity" dropdown restricted users to predefined options, which did not support partial or case-insensitive searches. This made it difficult for users to filter based on personalized inputs.

Root Cause: The backend query relied on exact matches, which excluded valid results with slight variations in spelling or case (e.g., "Shiva" vs. "shiva").

Resolution: The dropdown was replaced with a free-text input field. Validation was added to ensure clean inputs (pattern="^[a-zA-Z0-9 ]{2,90}$"). The backend was enhanced to use MongoDB's $regex operator with case-insensitive matching, allowing more flexible filtering.

**4. Delete Functionality Did Not Work Consistently**
Bug Encountered: The delete functionality for both sites and journey insights did not always remove the correct entries. This led to confusion and created data inconsistencies.

Root Cause: Improper usage of ObjectId during deletion attempts caused invalid MongoDB queries, resulting in no action being taken.

Resolution: Validation was added to ensure that valid ObjectId values were passed to the delete queries. Error handling was also improved to provide clear feedback when deletions failed due to invalid or missing IDs.

**5. Edit Functionality Validation**
Bug Encountered: Users could submit incomplete or invalid data when editing entries, leading to malformed or broken records in the database.

Root Cause: Validation for required fields was either absent or improperly implemented in the frontend forms and backend routes.

Resolution: Comprehensive validation logic was added to both the frontend and backend to ensure all fields were filled out before submission. Backend logic was adjusted to reject invalid updates and provide informative error messages.

**6. Usability Enhancements: Adding Links to Home Page**
Bug Encountered: The homepage did not include intuitive navigation links to key sections like "Browse Sites" and "Journey Insights," forcing users to navigate through the top menu.

Root Cause: A lack of design foresight during the initial UI implementation.

Resolution: Hyperlinks were added to the "Browse Sites" and "Journey Insights" cards on the homepage. These links guide users directly to the respective sections, improving the overall navigation experience.

**7. Visual Enhancements: Color and Typography**
Bug Encountered: The application had inconsistent typography and color schemes across pages, leading to a lack of visual coherence. Important messages and elements lacked sufficient contrast, reducing readability.

Root Cause: Colors and typography were not aligned with a consistent design system during the initial implementation.

Resolution: The color scheme was standardized across the application, using contrasting tones for text and backgrounds to improve readability. Typography was adjusted for consistency and emphasis, with clear headings and appropriate font sizes for different sections.

**8. Cluttered "Read Insights" Page**
Bug Encountered: The "Read Insights" page displayed all journey details at once, overwhelming users and making it difficult to scan through entries.

Root Cause: The UI lacked an expandable or collapsible design, forcing users to scroll through unnecessary details for each entry.

Resolution: A collapsible structure was implemented, showing only the title, visit date, and rating by default. Additional details can be revealed by clicking on a specific entry. This improvement streamlined the layout and made it easier to navigate.

**9. Missing Validation for Materialize Select**
Bug Encountered: The select elements on the filter and form pages failed validation when users interacted with them improperly or skipped them entirely, even for optional fields.

Root Cause: Materialize select elements required additional logic to handle focus, blur, and selection states.

Resolution: Custom validation logic was implemented using JavaScript to dynamically mark select elements as valid or invalid based on user interaction. This ensured smoother form submission and reduced user frustration.

**10. Reset Button Behavior on Filters**
Bug Encountered: Clicking the "Reset" button did not fully clear the form fields or reload the page state. This caused filters to behave unpredictably after being reset.

Root Cause: The reset button was not programmed to reinitialize the dropdowns or clear backend queries.

Resolution: The "Reset" button was configured to reload the page entirely, ensuring that all filters were cleared and dropdowns were reset to their default states.

---

## **Database Structure**
- **Collections:**
    - `locations`: Stores site details like `site_name`, `deity`, and `part_name`.
    - `reviews`: Stores user insights with fields like `rating`, `purpose`, and `description`.

---

## **Technologies Used**
### Languages:
- Python, JavaScript (JQuery), HTML5, CSS3.
### Frameworks and Tools:
- Flask, MongoDB, Materialize CSS, Git, Heroku.

---

- ## Browser Compatibility
------------
* Testing has been carried out on the following browsers :
    - Chrome Version 120.0.6099.225 (Official Build) (64-bit)
    - Firefox Version 122.0 (64-bit)
    - Edge Version 121.0.2277.83 (Official build) (64-bit)
    All the functionalities and appearance works as intended on all the above browsers.

- ## Deployment and Cloning
------------- 
+ Deployment to Heroku:

    * Open a command line/terminal window within the main project folder. 
    * Create a requirements.txt file by typing `pip3 freeze --local > requirements.txt` at the command line.
    * Create a Procfile by typing `echo web: python app.py > Procfile` 
    * Add and commit these files to Github.
    * Go to (https://www.heroku.com/). Log in or create an account
    * Click the 'New' button and click 'Create new app'.
    * Enter a unique name for your project with no capital letters or spaces and select the region closest to you (e.g., Europe). Click 'Create App'.
    * Inside the dashboard for your new app, go to the 'Settings' tab. 
    * Scroll down and click 'Reveal Config Vars' then enter data for the following variables:
    - `IP : 0.0.0.0`
    - `PORT : 5000`
    - `MONGO_DBNAME : ...` Your MongoDB database name
    - `MONGO_URI : ...` Your MongoBD URI (found on MongoDB by going to Clusters > Connect > Connect to your application)
    - `SECRET_KEY : ...` Your secret key
    * Link Github repo to Heroku by navigating to the Deploy tab. Select 'GitHub, enter the name of the repository and click connect. 
    * Once connected, select the repo branch to deploy (e.g. main) then click the Enable Automatic Deployment option.
    * To deploy immediately, in the Manual Deploy section again select the branch you want to deploy and click Deploy Branch. This will retrieve the code from GitHub. Once this is complete you'll receive a message "Your app was successfully deployed." You can then click "View" to access the deployed app.
    * 


+ Cloning:

    * visit url - https://github.com/ashwinsel/Milestone-Project-2 this will open the repository on Github
    * Click on the "Code" green coloured button to the right of the screen, click HTTPs and copy the link there
    * Open a GitBash terminal and navigate to the directory where you want to locate the clone
    * On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process

- ## Credits
------------
- ### Content
    * Some inputs regarding sites has been adapted from https://www.visa-indian-online.org/the-full-guide-to-spiritual-tourism-in-india 
    ![def33]
    * All other content has been drafted by the developer.

- ### Code
    * Code on how to present a modal and close was created with the help of a tutorial on [WebDevSimplified][def76].
    * Code for the hover effect on info cards on Home page was an play around with some examples from  [Codepen]
    * I have used Materialize code to implement various aspects of the website.
    * The basic logic has been based on a tutorial by Tim Nelson, Task Manager Walkthrough.
    * Hover effects on throughout has been created by using tutorials on [W3schools](https://www.w3schools.com/cssref/sel_hover.php)
    * Datepicker aspect and some other code adapted from Task Manager Walkthourgh on Code Institute by Tim Nelson
    * Slider code was inspired by Hitesh Choudhary

- ### Media
    * ![Favicon]![def4] a vector art by https://www.shutterstock.com/g/iostephy
    * [Background Image]![def46]

- ## Gratitude
    * I would like to thank my mentor Dick Vlaanderen for all the coaching and helping me with their insight and experience.
    * Thanks to tutor Rebecca and Alan, who helped me fix my connection to MOngoDB.
    * Thank you to Hitesh Chaudhary for the lessons on ChaiCode.com.
    * Thanks to various contributors on StackOverflow.
    * Thanks to Amy our facilitator for running our regular Stand-ups which gave me confidence.
    * Thanks to Code with Harry on tutorial videos re Python and PyMongo






[Cdnfonts]: https://www.cdnfonts.com/samarkan.font
[def0]: https://travelmoves.in/india-news/indias-travel-trends-surge-in-spiritual-destination-searches
[def1]: ./documentation/favicon.png
[def2]: #c-frequent-user-goals
[def3]: #future-implementations
[def4]: https://www.shutterstock.com/g/iostephy
[def6]: ./documentation/validatorresults.png
[def7]: ./documentation/firstlighthouseresult.png
[def8]: ./documentation/lighthousetesting2.png
[def9]: https://fontawesome.com/
[def10]: https://ashwinsel-milestone1-shxwdq7nqt6.ws-eu107.gitpod.io/
[def11]: https://github.com/ashwinsel/Milestone-1.git
[def12]: https://www.microsoft.com/en-gb/microsoft-365/powerpoint
[def13]: https://balsamiq.com/
[def14]: https://coolors.co/
[def15]: https://tinypng.com/
[def16]: ./documentation/testcasesandresults.png
[def17]: https://materializecss.com/about.html
[def18]: https://autoprefixer.github.io/
[def19]: https://favicon.io/
[def20]: https://validator.w3.org/
[def21]: https://linktr.ee/iamavinashkr
[def22]: https://ui.dev/amiresponsive?url=https://ashwinsel.github.io/Milestone-1/index.html
[def23]: https://www.freeformatter.com/html-formatter.html
[def24]: ./documentation/home-ss.png
[def25]: ./documentation/flowchart1.png
[def26]: ./documentation/home-ss.png
[def27]: ./documentation/ss-browsesites.png
[def28]: ./documentation/ss-addinsight.png
[def29]: ./documentation/colour-pallete.png
[def30]: ./documentation/ss-register.png
[def31]: ./documentation/ss-signin.png
[def32]: ./documentation/ss-readinsight.png
[def33]: https://www.visa-indian-online.org/the-full-guide-to-spiritual-tourism-in-india
[def34]: ./documentation/error1.png 
[def42]: https://yatra1-4cc0076860db.herokuapp.com/ 
[def45]: ./documentation/lt-addsite.png
[def46]: ./documentation/main-img.png
[def47]: ./documentation/lt-addsite.png
[def49]: ./static/img/chakra.png
[def50]: ./documentation/lt-home.png
[def64]: ./documentation/lt-browsesites.png
[def65]: ./documentation/lt-readinsight.png
[def66]: ./documentation/lt-register.png
[def67]: ./documentation/lt-signin.png
[def68]: ./documentation/lt-addinsight.png
[def74]: ./documentation/traceability-matrix.png
[def75]: https://www.jagranjosh.com/general-knowledge/gk-quiz-on-hindu-mythology-1706194424-1
[def76]: https://courses.webdevsimplified.com/