using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CubeSCR : MonoBehaviour
{
    int control = 1;
    private Rigidbody rb;
    private MeshRenderer mr;
    public Material normalPlayerColor;
    public Material jumpPlayerColor;
    public float jumpPower = 300;
    public float speed = 0;
    public LayerMask ground;
    public GameObject feet;
    public bool isJumpBoostActive = false;
    private AudioSource sound_player;



    void Start()
    {
        mr = GetComponent<MeshRenderer>();
        rb = GetComponent<Rigidbody>();
        sound_player = GetComponent<AudioSource>();



    }

    void Update()
    {
        if (Input.GetKey(KeyCode.W))
        {
            transform.position += Vector3.forward * speed * Time.deltaTime;
        }

        if (Input.GetKey(KeyCode.S))
        {
            transform.position += Vector3.back * speed * Time.deltaTime;
        }

        if (Input.GetKey(KeyCode.D))
        {
            transform.position += Vector3.right * speed * Time.deltaTime;
        }

        if (Input.GetKey(KeyCode.A))
        {
            transform.position += Vector3.left * speed * Time.deltaTime;
        }
        isGrounded();
        Vector3 jump = new Vector3(0, jumpPower, 0);
        if (Input.GetKeyDown(KeyCode.Space) && isGrounded())
        {
            rb.AddForce(jump);
            sound_player.Play();

        }




    }



    bool isGrounded()
    {
        Collider[] groundCheck = Physics.OverlapSphere(feet.transform.position, 0.1f, ground);
        if (groundCheck.Length > 0)
        {
            Debug.Log("We have touched the ground");
            return true;
        }

        return false;
    }




}
